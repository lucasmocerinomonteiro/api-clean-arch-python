"""
to instance this class we need the DeleteUserInteractor to do the delete 
"""
class DeleteUserController:
    def __init__(self, interactor, user_id):
        self.interactor = interactor
        self.user_id = user_id
    
    def handle(self):
        try:
            return self.interactor.delete_user_of_database(self.user_id)
        except:
            print("Error On DeleteUserController")