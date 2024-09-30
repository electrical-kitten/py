class AnonymousSurvey:
    """collect anonymous answers"""

    def __init__(self, question):
        """ store question and prepare to store the answers"""

        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question"""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the response that have been given"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")