import smartpy as sp

class PointsData(sp.Contract):
    def __init__(self):
        self.init(pointsMap = sp.map())

    @sp.entry_point
    def createUser(self, params):
        username = params.username
        sp.if self.data.pointsMap.contains(username):
            sp.failwith('username already exists')
        self.data.pointsMap[username] = 0

    @sp.entry_point
    def updatePoints(self, params):
        username = params.username
        points = params.points
        self.checkUser(username)
        self.data.pointsMap[username] += points

    @sp.entry_point
    def deleteUser(self, params):
        username = params.username
        self.checkUser(username)
        del self.data.pointsMap[username]

    def checkUser(self, username):
        sp.verify(self.data.pointsMap.contains(username))



if "templates" not in __name__:
    @sp.add_test(name = "MyContract")
    def test():
        c1 = PointsData()
        html = sp.test_scenario()
        html += c1
        html += c1.createUser(
            username='anshit'
        )
        html += c1.updatePoints(username='anshit', points=20)
        html += c1.deleteUser(username='anshit')
