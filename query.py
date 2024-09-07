'''
CSCI 531 Final Project
Andrew Rodriguez
Aaron Lobo
'''

from audit import addRecord, checkAudit, addedComment, deletedComment
from crypt import encryptMessage,decryptMessage

auditServerPublicKey = 'auditServer.pub'
queryServerPrivateKey = 'queryServer.prv'

def queryPatient(name, user):
    encryptedName = encryptMessage(auditServerPublicKey, name, "name")
    encryptedUser = encryptMessage(auditServerPublicKey, user, "user")
    inputFile = open(f"EHR/{name}.txt", 'r')
    lines = inputFile.read()
    inputFile.close()
    print(lines)
    addRecord(encryptedName, encryptedUser)
    
    return lines

def checkPatientAudit(name):
    encryptedName = encryptMessage(auditServerPublicKey, name, "name")
    result = checkAudit(encryptedName)
    decryptedResult = decryptMessage(queryServerPrivateKey,"records")
    return decryptedResult

def addHealthRecord(name, user, comment):
    encryptedName = encryptMessage(auditServerPublicKey, name, "name")
    encryptedUser = encryptMessage(auditServerPublicKey, user, "user")
    encryptedComment = encryptMessage(auditServerPublicKey, comment, "comment")
    with open(f"EHR/{name}.txt", 'a') as outFile:
        outFile.write("\n" + comment)
    addedComment(encryptedName, encryptedUser, encryptedComment)
    return str(comment + " has been added.")

def deleteHealthRecord(name, user, comment):
    encryptedName = encryptMessage(auditServerPublicKey, name, "name")
    encryptedUser = encryptMessage(auditServerPublicKey, user, "user")
    encryptedComment = encryptMessage(auditServerPublicKey, comment, "comment")
    inFile = open(f"EHR/{name}.txt", 'r')
    lines = inFile.readlines()
    inFile.close()
    lines = [line for line in lines if comment not in line]
    with open(f"EHR/{name}.txt", 'w') as outFile:
        outFile.writelines(lines)
    deletedComment(encryptedName, encryptedUser, encryptedComment)
    return str(comment + " has been deleted.")

