class QRReadError(IOError):
    """Raised when QRReader fails to fetch data from an image, or fetches
    obviously corrupted data"""
