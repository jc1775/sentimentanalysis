class InstagramAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = []
        self.photos = []
        self.following = []

    def follow(self, another_account):
        another_account.followers.append(self.username)
        self.following.append(another_account.username)

    def add_photo(self, photo):
        self.photos.append(photo)
    def get_followers(self):
        return self.followers, "You have " + str(len(self.followers)) + " followers"
    def __repr__(self):
        return f'<username: {self.username}, password: {self.password}, followers: {self.followers}, following: {self.following}, photos: {self.photos}>'




my_account = InstagramAccount('Joseph','1234568')
other_account = InstagramAccount('Evil CLone','123123123123')
third_account = InstagramAccount('Another Clone','1231241241241')

third_account.follow(other_account)
my_account.follow(other_account)
other_account.add_photo({'id':'12345','date taken': 'march 20 2011', 'url': 'http://1234567890qwerty', 'likes': '123456789012345678'})

print(other_account.get_followers())
print(my_account.photos)
print(other_account)
