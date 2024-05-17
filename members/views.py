from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse
from django.template import loader


def index(request):
  template=loader.get_template('index.html')
  return HttpResponse(template.render())

def post(request):
  template = loader.get_template('post_detail.html')
  return HttpResponse(template.render())

def contactWithUs(request):
  template = loader.get_template('contactWithUs.html')
  return HttpResponse(template.render())

def entertainment(request):
  template = loader.get_template('entertainment.html')
  return HttpResponse(template.render())

def submit(request):
  template = loader.get_template('submit.html')
  return HttpResponse(template.render())

def movies(request):
  template = loader.get_template('movies.html')
  return HttpResponse(template.render())
def songs(request):
  template = loader.get_template('songs.html')
  return HttpResponse(template.render())
def books(request):
  template = loader.get_template('books.html')
  return HttpResponse(template.render())

# from .forms import CommentForm
# from django.shortcuts import render, get_object_or_404

# def post_detail(request, slug):
#     template_name = 'post_detail.html'
#     post = get_object_or_404( slug=slug)
#     comments = post.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():

#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()

#     return render(request, template_name, {
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})


