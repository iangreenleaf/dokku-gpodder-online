#
# This file is part of my.gpodder.org.
#
# my.gpodder.org is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# my.gpodder.org is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public
# License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with my.gpodder.org. If not, see <http://www.gnu.org/licenses/>.
#

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from mygpo.api.models import Podcast, UserProfile, Episode, Device, EpisodeAction, SubscriptionAction

def home(request):
       if request.user.is_authenticated():
              subscriptionlist = create_subscriptionlist(request)              

              return render_to_response('home-user.html', {
                    'subscriptionlist': subscriptionlist
              }, context_instance=RequestContext(request))

       else:
              podcasts = Podcast.objects.count()
              return render_to_response('home.html', {
                    'podcast_count': podcasts
              })

def create_subscriptionlist(request):
      userid = UserProfile.objects.filter(user=request.user)[0].id
      device = Device.objects.filter(user__id=userid)
      device_ids = [d.id for d in device]
      sublog = SubscriptionAction.objects.filter(device__in=device_ids)
      sublog_podcastids = [s.podcast_id for s in sublog]
      podcast = Podcast.objects.filter(id__in=sublog_podcastids)
      subscriptionlist = [{'title': p.title, 'logo': p.logo_url, 'id': p.id} for p in podcast]
      for index, entry in enumerate(subscriptionlist):
            subscriptionlist[index]['episode'] = 'epi'
      return subscriptionlist

