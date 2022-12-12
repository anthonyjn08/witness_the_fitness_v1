from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm


@login_required
def add_post(request):
    """
    View to add a blog post.
    """
    print(request.user)
    post_form = PostForm(request.POST, request.FILES)

    if request.method == 'POST':
        if post_form.is_valid():
            post_form = post_form.save(commit=False)
            post_form.title = post_form.title
            post_form.author = request.user
            post_form.status = 1
            post_form.save()
            return redirect(reverse('blog'))

    context = {
        'post_form': post_form
    }

    return render(request, 'blog/add_post.html', context)


class EditPost(UpdateView):
    """
    View to edit post.
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/edit_post.html'
    success_url = '/blog/'


class DeletePost(DeleteView):
    """
    View for deletion of blog post.
    """
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/posts.html'
    paginate_by = 6


class PostDetail(View):
    """
    Post detail view to display blog post when clicked on.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        template = 'blog/post_detail.html'
        context = {
            "post": post,
            "comments": comments,
            "liked": liked,
            "comment_form": CommentForm(),
        }

        return render(request, template, context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.name = request.user
            comment.save()
            messages.success(request, 'Thanks for your comment')

        else:
            comment_form = CommentForm()

        template = 'blog/post_detail.html'
        context = {
            "post": post,
            "comments": comments,
            "liked": liked,
            "comment_form": CommentForm(),
        }

        return render(request, template, context)


class PostLike(View):
    """
    Post like view displays number of likes for recipe.
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.userprofile.id).exists():
            post.likes.remove(request.user.userprofile)
        else:
            post.likes.add(request.user.userprofile)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class DeleteComment(DeleteView):
    """
    Delete comment view.
    """
    model = Comment
    template_name = 'blog/delete_comment.html'
    success_url = reverse_lazy('blog')
