{% if page.status or page.path == "index.md" %}

Open Issues

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<script type="text/javascript"> GITHUB_ISSUES_USER = "iipc"; GITHUB_ISSUES_REPO = "warc-specifications"; /* Uncomment the following line to filter issues by one or more labels.*/ {% if page.version-of != %} GITHUB_ISSUES_LABELS = "{{ page.version-of }}"; {% endif %} /* To filter by multiple labels use a CSV string: */ // GITHUB_ISSUES_LABELS = "feature,bug"; </script>
<script> var GithubIssuesWidget = {}; GithubIssuesWidget.url = "https://api.github.com/repos/" + GITHUB_ISSUES_USER + "/" + GITHUB_ISSUES_REPO + "/issues?callback=?" if(typeof window.GITHUB_ISSUES_LABELS != "undefined") { GithubIssuesWidget.url += "&labels=" + GITHUB_ISSUES_LABELS; } GithubIssuesWidget.go = function () { $('#github-issues-widget').append('
Loading...

'); $.getJSON(this.url, function (data) { var list = $('
'); $.each(data.data, function (issueIndex, issue) { var issueHtml = "
"; issueHtml += ''; issueHtml += issue.title; issueHtml += ""; var style = ""; if( typeof issue.labels != "undefined") { $.each(issue.labels, function (labelIndex, label) { style = 'background-color:#' + label.color + ';'; if(label.color == "000000"){ style = 'color: white;' + style; } issueHtml += ' ' + label.name + ''; }); } issueHtml += "
"; list.append(issueHtml); }); $('#github-issues-widget p.loading').remove(); $('#github-issues-widget').append(list); }); }; GithubIssuesWidget.go(); </script>
{% endif %}
