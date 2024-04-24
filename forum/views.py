import random
import string
from django.db.models.query import QuerySet
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpRequest , HttpResponse
from forum.models import Post
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from users.models import User
from django.db.models import Q
from django.views.generic import ListView


# Create your views here.



class HomeView(ListView):
    template_name = 'index.html'
    context_object_name ='posts'
    paginate_by = 6
    def get_queryset(self):
         q = self.request.GET.get('q','')
         return Post.objects.filter(
             Q (title__icontains = q)
             | Q(author__username__icontains=q)
                
         )

       

    
        
        



@login_required
def about_views(request: HttpRequest)-> HttpResponse:

    return render(
        request,
        'about.html',
    )

@login_required
def post_create_views(request: HttpRequest,  )-> HttpResponse:
   
    

    print(request.user)
    print( 'post', request.POST) 
    print('get', request.GET)


    if request.method == 'POST':
        form = PostCreateForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            
            return redirect("home")
        
        return render(
          request,
          'post_create.html',
        {
            'form':form
        }
    ) 

    return render(

       request,

       'post_create.html',
        
        {
            'form':PostCreateForm()
        }



       
   )

          
@login_required
def post_delete_view(request: HttpRequest, post_id:int ) -> HttpResponse:
   
     post = get_object_or_404(request.user.post_set , pk = post_id)
    
     post.delete()
     return redirect('home')

   


@login_required
def random_post_create_view( request: HttpRequest)-> HttpResponse:
    post = Post(
        author = request.user,
        title = "".join(random.choices(string.ascii_letters , k=random.randint(10, 30))),
        content ="".join(random.choices(string.ascii_letters , k=random.randint(100 , 600)))
        

    )
    
    post.save()
    return redirect('home')
    
    
@login_required
def post_update_view(request: HttpRequest, pk: int)-> HttpResponse:
    post: Post = get_object_or_404(request.user.post_set,pk = pk)
    print(request.META.get('HTTP_REFERER'))
    

    if request.method == 'POST':
        form = PostCreateForm( request.POST,    instance= post)

        if form.is_valid():
            form.save()
            return redirect('home')
        return render (
              request,

        'post_update.html',
        context={
            'post': post,
            'form': form
        }


        )
        

    form = PostCreateForm( instance=post)

    return render(
        request,

        'post_update.html',
        context={
            'post': post,
            'form': form
        }

    )


def post_detail_view(request: HttpRequest , pk:int)-> HttpResponse:
    post: Post = get_object_or_404(Post , pk = pk)
    return render(
        request,
        'post_detail.html',
        context={
            'post':post,
            
            
        }
    )


          
        
       
    
    


    




    
   

 

        
    
