# HashCrack

HashFindr is a hash-finding utility designed for cybersecurity related Capture-the-Flag events. The utility is quickly able find MD5, SHA1, and SHA256 hash collisions given a complete or partial hash. The utility uses brute force methods and will print all found collisions. Implementations are provided in Java and Python, with the Java implementation being notably faster.

## Java - Requirements
None

## Java - Usage:
Compile:
```javac -cp ".;./commons-codec-1.10.jar;" .\JavaBrute.java```

Run:
```java -cp ".;./commons-codec-1.10.jar;" JavaBrute```

## Python - Requirements
```pip3 install click```

## Python - Usage
```python3 PyBrute.py```

