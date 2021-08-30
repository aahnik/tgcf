"""Declare all global constants."""

COMMANDS = {
    "start": "Check whether I am alive",
    "forward": "Set a new forward",
    "remove": "Remove an existing forward",
    "help": "Learn usage",
}

REGISTER_COMMANDS = True

KEEP_LAST_MANY = 10000

CONFIG_FILE_NAME = "tgcf.config.yml"
CONFIG_ENV_VAR_NAME = "TGCF_CONFIG"


class BotMessages:
    """Messages given by the bot to users."""

    # pylint: disable=too-few-public-methods

    # Available to users
    start = "Hi! I am alive"
    bot_help = "For details visit github.com/aahnik/tgcf"
    user_not_admin = "You are not authorized."

    # Available to administrators

    # /forward command
    forward_applied = "Success"
    display_forwards_empty = "Currently no forwards are set"
    forward_str_title = "This is your configuration"
    forward_str_source = "source:"
    forward_str_destination = "dest:"

    # /remove command
    remove_source_not_exists = "The source does not exist"
    remove_applied = "Success"

    # /style command
    style_applied = "Success"
    style_unexpected = "Invalid style. Choose from"  # "{style_unexpected} {_valid}"

    # usage of the commands
    forward_usage = """The `/forward` command allows you to add a new forward.
        Example: suppose you want to forward from a to (b and c)
    
        ```
        /forward source: a
        dest: [b,c]
        ```
    
        a,b,c are chat ids
    
        """.replace(
            "    ", ""
    )
    style_usage = """This command is used to set the style of the messages to be forwarded.
    
        Example: `/style bold`
    
        Options are preserve,normal,bold,italics,code, strike
    
        """.replace(
            "    ", ""
    )
    remove_usage = """The `/remove` command allows you to remove a source from forwarding.
        Example: Suppose you want to remove the channel with id -100, then run

        `/remove source: -100`

        """.replace(
        "    ", ""
    )
