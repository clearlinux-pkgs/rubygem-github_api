#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-github_api
Version  : 0.14.0
Release  : 8
URL      : https://rubygems.org/downloads/github_api-0.14.0.gem
Source0  : https://rubygems.org/downloads/github_api-0.14.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-addressable
BuildRequires : rubygem-bundler
BuildRequires : rubygem-hashie
BuildRequires : rubygem-oauth2
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc

%description
<div align="center">
<a href="http://piotrmurach.github.io/github/"><img width="136" src="https://github.com/piotrmurach/github/raw/master/icons/github_api.png" alt="github api logo" /></a>
</div>
# GithubAPI
[![Gem Version](https://badge.fury.io/rb/github_api.svg)][gem]
[![Build Status](https://secure.travis-ci.org/piotrmurach/github.svg?branch=master)][travis]
[![Code Climate](https://codeclimate.com/github/piotrmurach/github/badges/gpa.svg)][codeclimate]
[![Coverage Status](https://coveralls.io/repos/piotrmurach/github/badge.svg?branch=master)][coverage]
[![Inline docs](http://inch-ci.org/github/piotrmurach/github.svg)][inchpages]
[![Dependency Status](https://gemnasium.com/piotrmurach/github.svg?travis)][gemnasium]

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n github_api-0.14.0
gem spec %{SOURCE0} -l --ruby > rubygem-github_api.gemspec

%build
gem build rubygem-github_api.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
github_api-0.14.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/github_api-0.14.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/api.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/api/actions.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/api/arguments.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/api/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/api/config/property.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/api/config/property_set.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/api/factory.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/authorization.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/activity.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/activity/events.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/activity/feeds.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/activity/notifications.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/activity/starring.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/activity/watching.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/authorizations.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/authorizations/app.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/emojis.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/gists.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/gists/comments.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/git_data.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/git_data/blobs.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/git_data/commits.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/git_data/references.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/git_data/tags.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/git_data/trees.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/gitignore.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/issues.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/issues/assignees.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/issues/comments.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/issues/events.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/issues/labels.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/issues/milestones.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/markdown.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/meta.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/orgs.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/orgs/members.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/orgs/memberships.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/orgs/teams.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/pull_requests.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/pull_requests/comments.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/collaborators.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/comments.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/commits.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/contents.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/deployments.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/downloads.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/forks.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/hooks.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/keys.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/merging.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/pages.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/pub_sub_hubbub.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/releases.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/releases/assets.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/releases/tags.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/statistics.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/repos/statuses.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/say.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/scopes.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/search.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/search/legacy.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/users.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/users/emails.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/users/followers.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/client/users/keys.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/configuration.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/connection.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/constants.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/core_ext/array.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/core_ext/hash.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/core_ext/ordered_hash.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/deprecation.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error/bad_request.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error/client_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error/forbidden.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error/internal_server_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error/invalid_options.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error/not_acceptable.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error/not_found.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error/required_params.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error/service_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error/service_unavailable.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error/unauthorized.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error/unknown_media.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error/unknown_value.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error/unprocessable_entity.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/error/validations.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/ext/faraday.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/middleware.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/mime_type.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/normalizer.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/null_encoder.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/page_iterator.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/page_links.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/paged_request.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/pagination.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/parameter_filter.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/params_hash.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/rate_limit.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/request.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/request/basic_auth.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/request/jsonize.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/request/oauth2.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/request/verbs.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/requestable.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/resource.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/response.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/response/atom_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/response/header.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/response/jsonize.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/response/mashify.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/response/raise_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/response/xmlize.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/response_wrapper.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/ssl_certs/cacerts.pem
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/utils/url.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/validations.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/validations/format.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/validations/presence.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/validations/required.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/validations/token.rb
/usr/lib64/ruby/gems/2.3.0/gems/github_api-0.14.0/lib/github_api/version.rb
/usr/lib64/ruby/gems/2.3.0/specifications/github_api-0.14.0.gemspec
