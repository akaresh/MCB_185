#!/bin/sh

git filter-branch --env-filter '

OLD_EMAIL="Amalia@Amalia-Macbook.local"
CORRECT_NAME="Amalia Karesh"
CORRECT_EMAIL="58994466+akaresh@users.noreply.github.com"

if [ "$GIT_COMMITTER_EMAIL" = "Amalia@Amalia-Macbook.local" ]
then
    export GIT_COMMITTER_NAME="$Amalia Karesh"
    export GIT_COMMITTER_EMAIL="$58994466+akaresh@users.noreply.github.com"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$Amalia@Amalia-Macbook.local" ]
then
    export GIT_AUTHOR_NAME="$Amalia Karesh"
    export GIT_AUTHOR_EMAIL="$58994466+akaresh@users.noreply.github.com"
fi
' --tag-name-filter cat -- --branches --tags
