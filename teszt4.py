class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password  # Non-public password storage
        self.albums = {}

    def check_password(self, password):
        return self._password == password

    def create_album(self, album_name):
        if album_name not in self.albums:
            self.albums[album_name] = Album(album_name, self)
            return True
        return False

    def delete_album(self, album_name):
        if album_name in self.albums:
            del self.albums[album_name]
            return True
        return False

class Photo:
    def __init__(self, name, owner, size, format):
        self.name = name
        self.owner = owner
        self.size = size
        self.format = format

    def update_size(self, new_size):
        if self.owner.check_password(input("Enter your password to confirm: ")):
            self.size = new_size
            return True
        return False

    def update_format(self, new_format):
        if self.owner.check_password(input("Enter your password to confirm: ")):
            self.format = new_format
            return True
        return False

class Album:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.photos = {}

    def add_photo(self, photo):
        if photo.owner == self.owner:
            self.photos[photo.name] = photo
            return True
        return False

    def remove_photo(self, photo_name):
        if photo_name in self.photos:
            del self.photos[photo_name]
            return True
        return False
