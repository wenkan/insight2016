import sys

users={}

batch = open(sys.argv[1],'r')

lines = batch.readlines()

for line in lines[1:]:
    elements = line.split(", ")
    user1 = elements[1]
    user2 = elements[2]
    if user1 in users:
        if user2 not in users[user1]:
            users[user1].append(user2)
    else:
        users[user1]=[user2]
    if user2 in users:
        if user1 not in users[user2]:
            users[user2].append(user1)
    else:
        users[user2]=[user1]


def searchFriends(source, target, track, degree, limit):
    if source not in users:
        return False
    if target in users[source]:
        return True
    elif degree < limit:
        track.append(source)
        for user in users[source]:
            if user not in track:
                if searchFriends(user, target, track, degree+1, limit):
                    return True
        return False
    else:
        return False


stream = open(sys.argv[2],'r')

output1 = open(sys.argv[3],'w')
output2 = open(sys.argv[4],'w')
output3 = open(sys.argv[5],'w')

transes = stream.readlines()

for trans in transes[1:]:
    fields = trans.split(", ")
    id1 = fields[1]
    id2 = fields[2]
    if searchFriends(id1, id2, [], 1, 1):
        output1.write("trusted\n")
    else:
        output1.write("unverified\n")
    if searchFriends(id1, id2, [], 1, 2):
        output2.write("trusted\n")
    else:
        output2.write("unverified\n")
    if searchFriends(id1, id2, [], 1, 4):
        output3.write("trusted\n")
    else:
        output3.write("unverified\n")





