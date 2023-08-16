from pathlib import Path
import logging
from PyQt6.QtGui import QIcon

logger = logging.getLogger(__name__)

class Icons:

    """This class provides various assets for the different modules."""

    @staticmethod
    def load_icon(folder, name):
        """Loads an icon and returns it as a QIcon.

        Args:
            folder (str): The folder in which the image is located.
            name (str): The name of the image to load.

        Returns:
            QIcon: The loaded image.
        """
        path = Path(__file__).parent / folder / name
        icon = QIcon(str(path))

        # Print warning if the icon could not be loaded
        if icon.availableSizes() == []:
            logger.warning(f"Could not load icon: {path}")

        return icon

class Logos(Icons):

    """This class provides the logos for the different modules."""

    @staticmethod
    def get_logo(name):
        """Returns a logo as a QIcon.

        Args:
            name (str): The name of the logo to load.

        Returns:
            QIcon: The loaded logo.
        """
        return Icons.load_icon("logos", name)

    @staticmethod
    def ArrowLeft12x12():
        """Returns the ArrowLeft_12x12 logo as a QIcon.

        Returns:
            QIcon: The ArrowLeft_12x12 logo.
        """
        return Logos.get_logo("ArrowLeft_12x12.png")

    @staticmethod
    def ArrowRight12x12():
        """Returns the ArrowRight_12x12 logo as a QIcon.

        Returns:
            QIcon: The ArrowRight_12x12 logo.
        """
        return Logos.get_logo("ArrowRight_12x12.png")

    @staticmethod
    def Garbage12x12():
        """Returns the Garbage_12x12 logo as a QIcon.

        Returns:
            QIcon: The Garbage_12x12 logo.
        """
        return Logos.get_logo("Garbage_12x12.png")

    @staticmethod
    def Pen12x12():
        """Returns the Pen_12x12 logo as a QIcon.

        Returns:
            QIcon: The Pen_12x12 logo.
        """
        return Logos.get_logo("Pen_12x12.png")

    @staticmethod
    def New16x16():
        """Returns the New_16x16 logo as a QIcon.

        Returns:
            QIcon: The New_16x16 logo.
        """
        return Logos.get_logo("New_16x16.png")

    @staticmethod
    def Load16x16():
        """Returns the Load_16x16 logo as a QIcon.

        Returns:
            QIcon: The Load_16x16 logo.
        """
        return Logos.get_logo("Load_16x16.png")

    @staticmethod
    def Save16x16():
        """Returns the Save_16x16 logo as a QIcon.

        Returns:
            QIcon: The Save_16x16 logo.
        """
        return Logos.get_logo("Save_16x16.png")
    
    @staticmethod
    def QuestionMark_16x16():
        """Returns the QuestionMark_16x16 logo as a QIcon.

        Returns:
            QIcon: The QuestionMark_16x16 logo.
        """
        return Logos.get_logo("QuestionMark_16x16.png")


class PulseParamters(Icons):

    """This class provides the pulse parameter assets for the different modules."""
    
    @staticmethod
    def get_pulseparameter(name):
        """Returns a pulse parameter as a QIcon.

        Args:
            name (str): The name of the pulse parameter to load.

        Returns:
            QIcon: The loaded pulse parameter.
        """
        return Icons.load_icon("pulseparameters", name)

    @staticmethod
    def GateOff():
        """Returns the GateOff logo as a QIcon.

        Returns:
            QIcon: The GateOff logo.
        """
        return PulseParamters.get_pulseparameter("GateOff.png")

    @staticmethod
    def GateOn():
        """Returns the GateOn logo as a QIcon.

        Returns:
            QIcon: The GateOn logo.
        """
        return PulseParamters.get_pulseparameter("GateOn.png")

    @staticmethod
    def RXOff():
        """Returns the RXOff logo as a QIcon.

        Returns:
            QIcon: The RXOff logo.
        """
        return PulseParamters.get_pulseparameter("RXOff.png")

    @staticmethod
    def RXOn():
        """Returns the RXOn logo as a QIcon.

        Returns:
            QIcon: The RXOn logo.
        """
        return PulseParamters.get_pulseparameter("RXOn.png")

    @staticmethod
    def TXCustom():
        """Returns the TXCustom logo as a QIcon.

        Returns:
            QIcon: The TXCustom logo.
        """
        return PulseParamters.get_pulseparameter("TXCustom.png")

    @staticmethod
    def TXGauss():
        """Returns the TXGauss logo as a QIcon.

        Returns:
            QIcon: The TXGauss logo.
        """
        return PulseParamters.get_pulseparameter("TXGauss.png")

    @staticmethod
    def TXOff():
        """Returns the TXOff logo as a QIcon.

        Returns:
            QIcon: The TXOff logo.
        """
        return PulseParamters.get_pulseparameter("TXOff.png")

    @staticmethod
    def TXRect():
        """Returns the TXRect logo as a QIcon.

        Returns:
            QIcon: The TXRect logo.
        """
        return PulseParamters.get_pulseparameter("TXRect.png")

    @staticmethod
    def TXSinc():
        """Returns the TXSinc logo as a QIcon.

        Returns:
            QIcon: The TXSinc logo.
        """
        return PulseParamters.get_pulseparameter("TXSinc.png")
