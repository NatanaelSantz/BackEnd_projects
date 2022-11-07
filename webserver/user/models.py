from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)


class UsuarioManager(BaseUserManager):

    def create_user(self, email, password=None):
        usuarios = self.model(
            email=self.normalize_email(email)
        )
        usuarios.is_active = True
        usuarios.is_staff = False
        usuarios.is_superuser = False
        if password:
            usuarios.set_password(password)
        usuarios.save()
        return usuarios

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.set_password(password)
        usuario.save()
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
