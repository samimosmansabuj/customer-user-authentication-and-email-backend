from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password, phone_number, **extra_field):
        if not username:
            raise ValueError('Username must be set!')
        if not email:
            raise ValueError('Email must be set!')
        if not phone_number:
            raise ValueError('Phone Number must be set!')
        
        user = self.model(
            username = username, email = email, phone_number = phone_number, **extra_field
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, username, email, phone_number, password, **extra_field):
        user = self.create_user(
            username = username, password=password, email = email, phone_number = phone_number, **extra_field
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
    