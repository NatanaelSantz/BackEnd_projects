from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)


class UsuarioManager(BaseUserManager):

    def create_user(self, email, password):
        usuarios = self.model(
            email=self.normalize_email(email)
        )
        User.is_active = True
        User.is_staff = False
        User.is_superuser = False
        if password:
            User.set_password(password)
        User.save()
        return usuarios

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        User.is_active = True
        User.is_staff = True
        User.is_superuser = True
        User.set_password(password)
        User.save()
        return usuario


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="E-mail dos usuários",
        max_length=200,
        unique=True,
    )
    is_active = models.BooleanField(
        verbose_name="Usuário está ativo",
        default=True,
    )

    is_staff = models.BooleanField(
        verbose_name="O Usuário é um adm de desenvolvimento",
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name="O Usuário é um super Usuário",
        default=False,
    )
    USERNAME_FIELD = "email"
    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuarios"

        def __str__(self) -> str:
            return self.email
