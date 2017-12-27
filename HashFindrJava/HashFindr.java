import java.security.MessageDigest;
import java.nio.charset.StandardCharsets;

import org.apache.commons.codec.binary.Hex;

public class HashFindr {

	// define modes
	private enum Mode {
		STARTS_WITH, ENDS_WITH, CONTAINS;
	}

	/* ADJUST PARAMETERS BELOW */

	// All possible characters in desired hash
	private static final String CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!\"'$%&/()=?";

	// Possible Algorithms: MD5, SHA-1, SHA-256
	private static final String ALGO = "SHA-1";

	// Possible Locations: STARTS_WITH, ENDS_WITH, CONTAINS
	private static final Mode HASH_LOCATION = Mode.CONTAINS;

	// Partial hash to match against
	private static final String PARTIAL_HASH = "hghbv";

	/* END ADJUST PARAMETERS */
	
	public static void main(String[] args) throws Exception {
		
		System.out.println("Working... ");

		// get starting time
		long startTime = System.currentTimeMillis();

		// initialize objects
		MessageDigest md = MessageDigest.getInstance(ALGO);
		
		// convert hash to lower case
		String hash = PARTIAL_HASH.toLowerCase();

		// generate all permutations of the charset
		new StringGen() {
			public void element(char[] result, int offset, int length) {
				
				String tempPass = new String(result, offset, length);
				String calcHash = new String(Hex.encodeHex(md.digest(tempPass.getBytes(StandardCharsets.UTF_8))));
				
				// check if hash is correct
				if (HASH_LOCATION == Mode.STARTS_WITH) {
					if (calcHash.startsWith(hash)) {
						System.out.format("Pass: %s \t Time: %f \t Hash: %s\n", tempPass, (System.currentTimeMillis() - startTime) / 1000.0, calcHash);
					}
				} else if (HASH_LOCATION == Mode.ENDS_WITH) {
					if (calcHash.endsWith(hash)) {
						System.out.format("Pass: %s \t Time: %f \t Hash: %s\n", tempPass, (System.currentTimeMillis() - startTime) / 1000.0, calcHash);
					}
				} else if (HASH_LOCATION == Mode.CONTAINS) {
					if (calcHash.contains(hash)) {
						System.out.format("Pass: %s \t Time: %f \t Hash: %s\n", tempPass, (System.currentTimeMillis() - startTime) / 1000.0, calcHash);
					}
				}
			}
			
		}.generate(CHARSET);

	}

}
