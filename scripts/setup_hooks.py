from envsync.hooks import create_post_checkout_hook, create_pre_commit_hook, create_post_merge_hook

if __name__ == "__main__":
    create_post_checkout_hook()
    create_pre_commit_hook()
    create_post_merge_hook()