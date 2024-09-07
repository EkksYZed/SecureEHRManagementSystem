'''
CSCI 531 Final Project
Andrew Rodriguez
Aaron Lobo
'''


from datetime import datetime, timezone
from crypt import decryptMessage,encryptMessage,encrypt,decrypt
import hashlib
from hashlib import sha256
import os
auditFile = "auditRecord.txt"
encryptedAuditRecord = "encryptedAuditRecord.cip"
auditPrivateKeyFile = "auditServer.prv"
auditPublicKeyFile = "auditServer.pub"
queryPublicKeyFile = "queryServer.pub"
decryptedAuditRecord = "decryptedAuditRecord.txt"

def addRecord(name, user):
    decryptAuditRecord(encryptedAuditRecord)

    checkHash(decryptedAuditRecord)
    decryptedName = decryptMessage(auditPrivateKeyFile, "name")
    decryptedUser = decryptMessage(auditPrivateKeyFile, "user")
    currentTime = datetime.now(timezone.utc)
    with open(decryptedAuditRecord, 'a') as outFile:
        outFile.write(f"{decryptedUser} has accessed {decryptedName}'s EHR record at {currentTime}\n")
    updateHash(decryptedAuditRecord)
    encryptAuditRecord(decryptedAuditRecord)

def addedComment(name, user, comment):
    decryptAuditRecord(encryptedAuditRecord)
    checkHash(decryptedAuditRecord)
    decryptedName = decryptMessage(auditPrivateKeyFile, "name")
    decryptedUser = decryptMessage(auditPrivateKeyFile, "user")
    decryptedComment = decryptMessage(auditPrivateKeyFile, "comment")
    currentTime = datetime.now(timezone.utc)
    with open(decryptedAuditRecord, 'a') as outFile:
        outFile.write(f"{decryptedUser} has added '{decryptedComment}' to {decryptedName}'s EHR record at {currentTime}\n")
    updateHash(decryptedAuditRecord)
    encryptAuditRecord(decryptedAuditRecord)

def deletedComment(name, user, comment):
    decryptAuditRecord(encryptedAuditRecord)
    checkHash(decryptedAuditRecord)
    decryptedName = decryptMessage(auditPrivateKeyFile, "name")
    decryptedUser = decryptMessage(auditPrivateKeyFile, "user")
    decryptedComment = decryptMessage(auditPrivateKeyFile, "comment")
    currentTime = datetime.now(timezone.utc)
    with open(decryptedAuditRecord, 'a') as outFile:
        outFile.write(f"{decryptedUser} has deleted '{decryptedComment}' from {decryptedName}'s EHR record at {currentTime}\n")
    updateHash(decryptedAuditRecord)
    encryptAuditRecord(decryptedAuditRecord)

def checkAudit(name):
    decryptAuditRecord("encryptedAuditRecord.cip")
    checkHash(decryptedAuditRecord)
    decryptedName = decryptMessage(auditPrivateKeyFile, "name")
    records = ''
    auditFile = "decryptedAuditRecord.txt"
    with open(decryptedAuditRecord, 'r') as inFile:
        lines = inFile.readlines()
        for line in lines:
            if decryptedName in str(line):
                records += line + "\n"
    enncryptedRecords = encryptMessage(queryPublicKeyFile,records,"records")
    updateHash(decryptedAuditRecord)
    encryptAuditRecord(decryptedAuditRecord)
    
    return enncryptedRecords

def updateHash(auditFile):
    hash = hashlib.sha1()
    with open(auditFile,'rb',buffering=0) as inFile:
        while True:
            chunk = inFile.read(hash.block_size)
            if not chunk:
                break
            hash.update(chunk)
    
    encryptedHash = encryptMessage(auditPublicKeyFile, hash.hexdigest(),"hash")

def checkHash(auditFile):
    decryptedHash = decryptMessage(auditPrivateKeyFile, "hash")
    hash = hashlib.sha1()
    with open(auditFile,'rb',buffering=0) as inFile:
        while True:
            chunk = inFile.read(hash.block_size)
            if not chunk:
                break
            hash.update(chunk)
    hash = hash.hexdigest()
    print(decryptedHash)
    print(hash)

    if str(decryptedHash) != str(hash):
        print("ERROR Audit record has been tampered with")


def encryptAuditRecord(auditFile):
    encryptedRecord = encrypt(auditPublicKeyFile,auditFile,"encryptedAuditRecord.cip")
    try:
        os.remove(decryptedAuditRecord)
    except:
        print("No audit Record")
        aFile = open("auditRecord.txt")
        encryptAuditRecord(aFile)

    return "encryptedAuditRecord.cip"

def decryptAuditRecord(auditFile):
    decryptedAuditRecord = decrypt(auditPrivateKeyFile,"encryptedAuditRecord.cip")
    with open("decryptedAuditRecord.txt","w") as outFile:
        for line in decryptedAuditRecord:
            outFile.write(line)



#encryptAuditRecord("auditRecord.txt")
#decryptAuditRecord("encryptedAuditRecord.txt")
