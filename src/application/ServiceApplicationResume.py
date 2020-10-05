from ..repository.ResumeRepository import InterfaceResumeRepository


class ServiceApplicationResume:
    def __init__(self, repoResume: InterfaceResumeRepository) -> None:
        self.repoResume = repoResume

    def getResume(self, language: str):
        return self.repoResume.getResume(language)
