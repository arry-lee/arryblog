from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
	"""docstring for LoginRequired"""
	@classmethod
	def as_view(cls,**initkwargs):
		view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
		return login_required(view)