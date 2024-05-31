from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

    def to_dict(self):
        """
        Convert the User object to a dictionary.

        Returns:
            dict: A dictionary representation of the User object.
        """
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
        }

    @staticmethod
    def get_user(id):
        """
        Retrieve a user by their ID.

        Args:
            id (int): The ID of the user.

        Returns:
            User: The User object if found, else None.
        """
        return User.query.filter_by(id=id).first()

    @staticmethod
    def get_login(data):
        """
        Authenticate a user by their email and password.

        Args:
            data (dict): A dictionary containing 'email' and 'password'.

        Raises:
            ValueError: If email or password is missing, or 
            if authentication fails.

        Returns:
            User: The authenticated User object.
        """
        if 'email' not in data or 'password' not in data:
            raise ValueError("Missing parameter")

        user = User.query.filter_by(email=data['email']).first()
        if not user:
            raise ValueError("Email doesn't exist")

        if check_password_hash(user.password, data["password"]):
            return user

        raise ValueError("Bad password")

    @staticmethod
    def get_users():
        """
        Retrieve all users.

        Returns:
            list: A list of all User objects.
        """
        return User.query.all()

    @staticmethod
    def create_user(data):
        """
        Create a new user.

        Args:
            data (dict): A dictionary containing 'email', 'name', 
            and 'password'.

        Raises:
            ValueError: If any required parameter is missing or 
            if the email already exists.

        Returns:
            User: The newly created User object.
        """
        if 'email' not in data or 'name' not in data or 'password' not in data:
            raise ValueError("Missing parameter")

        if User.query.filter_by(email=data['email']).first():
            raise ValueError("Email already exists")

        password_hash = generate_password_hash(data["password"],
                                               method="sha256")
        new_user = User(email=data["email"], name=data["name"],
                        password=password_hash)

        db.session.add(new_user)
        db.session.commit()

        return new_user

    def update_user(self, data):
        """
        Update the user's details.

        Args:
            data (dict): A dictionary containing 'email', 'name',
            and/or 'password'.

        Raises:
            ValueError: If any required parameter is missing.

        Returns:
            User: The updated User object.
        """
        if 'email' in data:
            self.email = data['email']
        if 'name' in data:
            self.name = data['name']
        if 'password' in data:
            self.password = generate_password_hash(data['password'],
                                                   method="sha256")

        db.session.commit()

        return self

    def delete_user(self):
        """
        Delete the user.

        Returns:
            None
        """
        db.session.delete(self)
        db.session.commit()
