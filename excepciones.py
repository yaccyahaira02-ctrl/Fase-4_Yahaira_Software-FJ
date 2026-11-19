# ARCHIVO 1: Excepciones personalizadas.
# Este archivo no necesita importar los otros archivos del proyecto.

# MÓDULO DE EXCEPCIONES PERSONALIZADAS
# ==========================================

class SoftwareFJError(Exception):
    """Excepción base para todos los errores personalizados de Software FJ."""
    pass # Clase principal que agrupa los errores del negocio

class ClienteInvalidoError(SoftwareFJError):
    """Se lanza cuando los datos de un cliente son inválidos o faltantes."""
    pass # Error específico para fallas en el registro del cliente

class ServicioNoDisponibleError(SoftwareFJError):
    """Se lanza cuando un servicio no está disponible o los parámetros son incorrectos."""
    pass # Error específico para fallas en los servicios

class ReservaInvalidaError(SoftwareFJError):
    """Se lanza cuando un intento de reserva falla por conflicto o datos erróneos."""
    pass # Error específico para fallas en el proceso de reservas

# ===========================================
