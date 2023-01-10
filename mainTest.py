
# This is a Unit Test file for the helper fuctions file.

from main import *
import unittest

# Unit tests specific for users type STUDENT:
if userObj.Usertype == "Student":

    class StudentTests(unittest.TestCase):

        #classes that we are gonna be testing:
        #=============Max=============#
        login = Login()
        signup = Signup()
        homepage = Homepage()
        password = Password()
        #===========Shay==============#
        usersettings = Usersettings()
        adPopup = AdPopup()
        myAds = MyAds()
        messagebox = MessageBox()
        generalmessage = GeneralMessagePopup()
        #===========Ivan==============#
        myAdsDetails = MyAdsDetails()
        studentResume = StudentResume()
        #=-----------------------------=#


        # Unit Tests for Login: 
            # None

        # Unit Tests for Signup: 
            # None

        # Unit Tests for Homepage: 
            # None

        # Unit Tests for Password: 
            # None

        # Unit Tests for Usersettings: 
        
        def test_Usersettings_To_Student_Resume(self):
            self.assertTrue(self.usersettings.change_to_student_resume)

        def test_Usersettings_To_Student_Report(self):
            self.assertTrue(self.usersettings.change_to_student_report)


        # Unit Tests for AdPopup: 


        # Unit Tests for MyAds: 


        # Unit Tests for MyAdsDetails: 

        # Unit Tests for MessageBox:
         
        # Unit Tests for GeneralMessage: 


        # Unit Tests for StudentResume:
        def test_handle_buttons(self):
            self.assertTrue(self.studentResume.handle_buttons)
        def test_save_changes(self):
            self.assertTrue(self.studentResume.save_changes)
        def test_edit_resume(self):
            self.assertTrue(self.studentResume.edit_resume)
        def test_change_to_usersettings(self):
            self.assertTrue(self.studentResume.change_to_usersettings)



#------------------------------------------------------#
# Unit tests specific for users type EMPLOYER:
if userObj.Usertype == "Employer":

    class EmployerTests(unittest.TestCase):

        #classes that we are gonna be testing:
        login = Login()
        signup = Signup()
        homepage = Homepage()
        password = Password()
        usersettings = Usersettings()
        adPopup = AdPopup()
        myAds = MyAds()
        messagebox = MessageBox()
        generalmessage = GeneralMessagePopup()
        myAdsDetails = MyAdsDetails()
        #newAd = NewAd() #<---- you cant create an object of this class without passing an argument, so try testing different class
        messageBox = MessageBox()
        #=-----------------------------=#
        
        # Unit Tests for Login:
            # None

        # Unit Tests for Signup:
            # None

        # Unit Tests for Homepage:
        def test_Homepage_To_NewAd(self):
            self.assertTrue(self.homepage.change_to_NewAd)
    
        def test_Homepage_To_My_Ads(self):
            self.assertTrue(self.homepage.change_to_my_ads)

        # Unit Tests for Password:
            # None

        # Unit Tests for Usersettings: 
        def test_Homepage_To_My_Ads(self):
            self.assertTrue(self.usersettings.change_to_my_ads)


        # Unit Tests for AdPopup: 


        # Unit Tests for NewAd: #<---- you cant create an object of this class without passing an argument, so try testing different class
        #def test_CreateAd(self):
        #    self.assertTrue(self.newAd.CreateAd)

        #def test_back_to_homepage(self):
        #    self.assertTrue(self.newAd.back_to_homepage)

        #def test_handle_buttons(self):
        #    self.assertTrue(self.newAd.handle_buttons)
        

        # Unit Tests for Usersettings: 
        def test_MessageBox_To_My_Ads(self):
            self.assertTrue(self.messageBox.SendMessageToAdmin)





#------------------------------------------------------#
# Unit tests specific for user type ADMIN:
if userObj.Usertype == "Admin":

    class AdminTests(unittest.TestCase):
        
        #classes that we are gonna be testing:
        login = Login()
        signup = Signup()
        homepage = Homepage()
        password = Password()
        usersettings = Usersettings()
        adPopup = AdPopup()
        myAds = MyAds()
        messagebox = MessageBox()
        generalmessage = GeneralMessagePopup()
        myAdsDetails = MyAdsDetails()
        messageBox = MessageBox() #exclusive for admin
        #=-----------------------------=#

        # Unit Tests for Login:
            # None

        # Unit Tests for Signup:
            # None

        # Unit Tests for Homepage:
        def test_Homepage_To_NewAd(self):
            self.assertTrue(self.homepage.change_to_NewAd)
    
        def test_Homepage_To_UserPopup(self):
            self.assertTrue(self.homepage.change_to_UserPopup)

        def test_Homepage_To_MessageBox(self):
            self.assertTrue(self.homepage.change_to_messageBox)
        
        
        # Unit Tests for Password:
            # None

        # Unit Tests for Usersettings: 
        def test_Usersettings_To_show_activity_window(self):
            self.assertTrue(self.usersettings.show_activity_window)

        # Unit Tests for AdPopup: 


        # Unit Tests for MyAds: 


        # Unit Tests for MessageBox: 
        

        def test_SendMessageFromAdmin(self):
            self.assertTrue(self.messagebox.SendMessageFromAdmin)

#------------------------------------------------------#
# Unit tests for EVERY USER TYPE together (these are mutual functions that we test):
class GeneralTests(unittest.TestCase):
        
    #classes that we are gonna be testing:
    login = Login()
    signup = Signup()
    homepage = Homepage()
    password = Password()
    usersettings = Usersettings()
    adPopup = AdPopup()
    myAds = MyAds()
    myAdsDetails = MyAdsDetails()
    messagebox = MessageBox()
    generalmessage = GeneralMessagePopup()
    myadsresume = MyAdsResumePopup()
    #=-----------------------------=#


    # Unit Tests for Login:
    def test_Login_To_Homepage(self):
        self.assertTrue(self.login.change_to_homepage)

    def test_Login_To_Signup(self):
        self.assertTrue(self.login.change_to_signup)

    def test_Login_To_Forgetpass(self):
        self.assertTrue(self.login.change_to_forgetpassword)
    
    def test_Login_Handle_Buttons(self):
        self.assertTrue(self.login.handle_buttons)



    # Unit Tests for Signup:
    def test_Signup_To_Homepage(self):
        self.assertTrue(self.signup.change_to_login)

    def test_Signup_Handle_Buttons(self):
        self.assertTrue(self.signup.handle_buttons)



    # Unit Tests for Homepage:
    def test_Homepage_To_Login(self):
        self.assertTrue(self.homepage.change_to_login)

    def test_Homepage_To_Handle_Buttons(self):
        self.assertTrue(self.homepage.handle_buttons)
    
    def test_Homepage_To_Usersettings(self):
        self.assertTrue(self.homepage.change_to_usersettings)
    
    def test_Homepage_To_AdvancedSearch(self):
        self.assertTrue(self.homepage.change_to_advanced_search)

    def test_Homepage_To_AdPopup(self):
        self.assertTrue(self.homepage.change_to_AdPopup)
    
    def test_Homepage_To_General_Message_Popup(self):
        self.assertTrue(self.homepage.change_to_generalMessagePopup)

    def test_Search(self):
        self.assertTrue(self.homepage.Search)

    def test_SearchAllJobs(self):
        self.assertTrue(self.homepage.SearchAllJobs)
    
    def test_SearchJob(self):
        self.assertTrue(self.homepage.SearchJob)

    def test_openChat(self):
        self.assertTrue(self.homepage.openChat)

    # Unit Tests for Password:
    def test_Password_To_Login(self):
        self.assertTrue(self.password.change_to_login)

    def test_Password_To_Handle_Buttons(self):
        self.assertTrue(self.password.handle_buttons)
    


    # Unit Tests for Usersettings: 
    def test_Usersettings_To_Handle_Buttons(self):
        self.assertTrue(self.usersettings.handle_buttons)
    
    def test_Usersettings_To_Login(self):
        self.assertTrue(self.usersettings.change_to_login)

    def test_Usersettings_To_Homepage(self):
        self.assertTrue(self.usersettings.back_to_homepage)

    def test_Usersettings_To_DeletePopup(self):
        self.assertTrue(self.usersettings.change_to_deletePopup)

    def test_Usersettings_To_Forgetpassword(self):
        self.assertTrue(self.usersettings.change_to_forgetpassword)

    def test_change_to_deletePopup(self):
        self.assertTrue(self.usersettings.change_to_deletePopup)

    def test_edit_personal_info(self):
        self.assertTrue(self.usersettings.edit_personal_info)

    def test_save_changes(self): #unit test for save notification settings and user info settings
        self.assertTrue(self.usersettings.save_changes)

    def test_change_to_deletePopup(self):
        self.assertTrue(self.usersettings.change_to_deletePopup)


    
    

    # Unit Tests for AdPopup: 
    def test_AdPopup_To_Handle_Buttons(self):
        self.assertTrue(self.adPopup.handle_buttons)
    
    def test_AdPopup_To_SendResume(self):
        self.assertTrue(self.adPopup.SendResume)

    def test_AdPopup_To_SendMessage(self):
        self.assertTrue(self.adPopup.SendMessage)

    def test_AdPopup_To_VisabilityPopUp(self):
        self.assertTrue(self.adPopup.VisabilityPopUp)

    def test_AdPopup_To_Change_to_EditAd(self):
        self.assertTrue(self.adPopup.Change_to_EditAd)

    def test_AdPopup_To_DeleteAd(self):
        self.assertTrue(self.adPopup.DeleteAd)

    def test_SetParameters(self):
        self.assertTrue(self.adPopup.SetParameters)

    def test_Change_to_EditAd(self):
        self.assertTrue(self.adPopup.Change_to_EditAd)

    def test_AdPopup_To_DeleteAd(self):
        self.assertTrue(self.adPopup.DeleteAd)
    



    # Unit Tests for MyAds: 
    def test_MyAds_To_handle_buttons(self):
        self.assertTrue(self.myAds.handle_buttons)
    
    def test_MyAds_To_login(self):
         self.assertTrue(self.myAds.change_to_login)

    def test_MyAds_To_usersettings(self):
         self.assertTrue(self.myAds.change_to_usersettings)

    def test_MyAds_To_homepage(self):
        self.assertTrue(self.myAds.change_to_homepage)

    def test_MyAds_To_NewAd(self):
         self.assertTrue(self.myAds.change_to_NewAd)

    def test_MyAds_To_myAdsDetails(self):
        self.assertTrue(self.myAds.change_to_myAdsDetails)
   



    # Unit Tests for MyAdsDetails: 
    def test_MyAdsDetails_To_handle_buttons(self):
        self.assertTrue(self.myAdsDetails.handle_buttons)
        
    def test_MyAdsDetails_To_EditAd(self):
        self.assertTrue(self.myAdsDetails.change_to_MyAds)
    
    def test_MyAdsDetails_To_ResumeFramePopup(self):
        self.assertTrue(self.myAdsDetails.change_to_ResumeFramePopup)

    #Unit Tests for MyAdsResumePopup:
    def test_SetParameters(self):
        self.assertTrue(self.myadsresume.SetParameters)

    def test_AcceptResume(self):
        self.assertTrue(self.myadsresume.AcceptResume)

    def test_RejectResume(self):
        self.assertTrue(self.myadsresume.RejectResume)

    def test_SendMessage(self):
        self.assertTrue(self.myadsresume.SendMessage)




    # Unit Tests for MessageBox:
    def test_SendMessageAdResume(self):
        self.assertTrue(self.messagebox.SendMessageAdResume)
    

    # Unit Tests for GeneralMessage: 
    def test_ShowMessages(self):
        self.assertTrue(self.generalmessage.ShowMessages)




if __name__ == '__main__':
    unittest.main()
