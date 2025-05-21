from django.core.exceptions import ValidationError


def validate_password(value):
    if len(value) < 8:
        raise ValidationError("Пароль должен содержать минимум 8 символов.")
    if not any(char.isdigit() for char in value):
        raise ValidationError("Пароль должен содержать хотя бы одну цифру.")
    if not any(char.isalpha() for char in value):
        raise ValidationError("Пароль должен содержать хотя бы одну букву.")
