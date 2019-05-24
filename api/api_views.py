from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from git import Repo
import time
from main_app.logger import django_logger


class Test(APIView):
    # authentication_classes = (SessionAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        repo = Repo()
        heads = repo.heads

        headcommit = heads.master.commit
        branch = repo.active_branch.name

        # user = request.user.username
        # django_logger.info(f'Test API user: {user}')
        return Response(
            {
                "commit": str(headcommit),
                "branch": str(branch),
                "commit_date": time.strftime("%Y-%m-%dT%H:%M", time.gmtime(headcommit.committed_date))

            }
        )
