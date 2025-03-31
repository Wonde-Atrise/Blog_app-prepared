from django.urls import path
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.Home,name='home'),
     
    path('login/',views.User_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.Register,name='register'),
     path('create-blog/',views.CreateBlog,name='create-blog'),
    path('user-profile/<str:username>',views.User_profile,name='user-p'),
      path('user-details/<str:username>',views.User_details,name='user-d'),

    path('details/<int:id>',views.Details,name='details'),

    path('update/<int:id>',views.Update_blog,name='update_blog'),

    path('delete/<int:id>',views.DeletBlog,name='delete_blog'),
    path('update-message/<int:id>',views.Updatemesags,name='update-message'),
    path('about/', views.About,name = 'about'),
    path('contact/',views.Contact, name ="Contact"),
    path('delte-message/<int:id>',views.delete_message,name='delete-message'),
    path('like/<int:id>',views.BlogLike,name='blog_like'),
    path('posts/',views.Posts,name='posts'),
    path('search-message/',views.searchBlog,name='search'),
    path('email-page/',views.SendEmail,name='sendemail'),
    
    #email reset functionality
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name="registration/password_rest_form.html"),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_c.html"),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/done.html"), name='password_reset_complete'),




]