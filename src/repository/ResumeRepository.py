import abc


class InterfaceResumeRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getResume(self, language: str):
        """
        get the resume Data based on the language 
        """
        raise NotImplementedError
