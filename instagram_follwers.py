import json

def get_unfollowers(followers_data, following_data, is_path=True):

    if is_path:

        with open(followers_data, 'r') as fp:
            data = json.load(fp)
            followers = {x['string_list_data'][0]['value'] for x in data}

        with open(following_data, 'r') as fp:
            data2 = json.load(fp)
            following = [x['string_list_data'][0]['value'] for x in data2['relationships_following']]

        not_following_back = []

        for x in following:
            if not x in followers:
                not_following_back.append(x)

        return not_following_back

    else:
        followers = {x['string_list_data'][0]['value'] for x in followers_data}
        following = [x['string_list_data'][0]['value'] for x in following_data['relationships_following']]
        
        for x in following:
            if not x in followers:
                not_following_back.append(x)

        return not_following_back

def get_removed_suggestions(removed_suggestions_data, is_path=True):
    if is_path:

        with open(removed_suggestions_data, 'r') as fp:
            data = json.load(fp)
            return [x['string_list_data'][0]['href'] for x in data['relationships_dismissed_suggested_users']]
        
    else:
        return [x['string_list_data'][0]['href'] for x in removed_suggestions_data['relationships_dismissed_suggested_users']]
