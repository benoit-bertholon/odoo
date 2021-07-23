# -*- coding: utf-8 -*-

{
    'name': 'Discuss',
    'version': '1.5',
    'category': 'Productivity/Discuss',
    'sequence': 145,
    'summary': 'Chat, mail gateway and private channels',
    'description': "",
    'website': 'https://www.odoo.com/app/discuss',
    'depends': ['base', 'base_setup', 'bus', 'web_tour'],
    'data': [
        'wizard/invite_view.xml',
        'wizard/mail_blacklist_remove_view.xml',
        'wizard/mail_compose_message_view.xml',
        'wizard/mail_resend_cancel_views.xml',
        'wizard/mail_resend_message_views.xml',
        'wizard/mail_template_preview_views.xml',
        'views/mail_message_subtype_views.xml',
        'views/mail_tracking_views.xml',
        'views/mail_notification_views.xml',
        'views/mail_message_views.xml',
        'views/mail_mail_views.xml',
        'views/mail_followers_views.xml',
        'views/mail_channel_partner_views.xml',
        'views/mail_channel_views.xml',
        'views/mail_shortcode_views.xml',
        'views/mail_activity_views.xml',
        'views/res_config_settings_views.xml',
        'data/ir_config_parameter_data.xml',
        'data/res_partner_data.xml',
        'data/mail_message_subtype_data.xml',
        'data/mail_templates.xml',
        'data/mail_channel_data.xml',
        'data/mail_activity_data.xml',
        'data/ir_cron_data.xml',
        'security/mail_security.xml',
        'security/ir.model.access.csv',
        'views/mail_alias_views.xml',
        'views/res_users_views.xml',
        'views/mail_template_views.xml',
        'views/ir_actions_views.xml',
        'views/ir_model_views.xml',
        'views/res_partner_views.xml',
        'views/mail_blacklist_views.xml',
        'views/mail_menus.xml',
    ],
    'demo': [
        'data/mail_channel_demo.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web._assets_primary_variables': [
            'mail/static/src/scss/variables.scss',
        ],
        'web.assets_backend': [
            'mail/static/src/js/core/translation.js',
            'mail/static/src/js/many2many_tags_email.js',
            'mail/static/src/js/m2x_avatar_user.js',
            'mail/static/src/js/field_char.js',
            'mail/static/src/js/document_viewer.js',
            'mail/static/src/js/basic_view.js',
            'mail/static/src/js/systray/systray_activity_menu.js',
            'mail/static/src/js/tours/mail.js',
            'mail/static/src/js/tools/debug_manager.js',
            'mail/static/src/js/custom_filter_item.js',
            'mail/static/src/js/utils.js',
            'mail/static/src/js/activity.js',
            'mail/static/src/js/views/activity/activity_view.js',
            'mail/static/src/js/views/activity/activity_model.js',
            'mail/static/src/js/views/activity/activity_controller.js',
            'mail/static/src/js/views/activity/activity_renderer.js',
            'mail/static/src/js/views/activity/activity_record.js',
            'mail/static/src/js/views/activity/activity_cell.js',
            'mail/static/src/js/emojis.js',
            'mail/static/src/js/emojis_mixin.js',
            'mail/static/src/js/field_emojis_common.js',
            'mail/static/src/js/field_char_emojis.js',
            'mail/static/src/js/field_text_emojis.js',
            'mail/static/src/scss/emojis.scss',
            'mail/static/src/variables.scss',
            'mail/static/src/scss/discuss.scss',
            'mail/static/src/scss/composer.scss',
            'mail/static/src/scss/thread.scss',
            'mail/static/src/scss/systray.scss',
            'mail/static/src/scss/mail_activity.scss',
            'mail/static/src/scss/m2x_avatar_user.scss',
            'mail/static/src/scss/activity_view.scss',
            'mail/static/src/scss/kanban_view.scss',
            'mail/static/src/component_hooks/use_drag_visible_dropzone/use_drag_visible_dropzone.js',
            'mail/static/src/component_hooks/use_refs/use_refs.js',
            'mail/static/src/component_hooks/use_rendered_values/use_rendered_values.js',
            'mail/static/src/component_hooks/use_should_update_based_on_props/use_should_update_based_on_props.js',
            'mail/static/src/component_hooks/use_store/use_store.js',
            'mail/static/src/component_hooks/use_update/use_update.js',
            'mail/static/src/components/activity/activity.js',
            'mail/static/src/components/activity_box/activity_box.js',
            'mail/static/src/components/activity_mark_done_popover/activity_mark_done_popover.js',
            'mail/static/src/components/attachment/attachment.js',
            'mail/static/src/components/attachment_box/attachment_box.js',
            'mail/static/src/components/attachment_delete_confirm_dialog/attachment_delete_confirm_dialog.js',
            'mail/static/src/components/attachment_list/attachment_list.js',
            'mail/static/src/components/attachment_viewer/attachment_viewer.js',
            'mail/static/src/components/autocomplete_input/autocomplete_input.js',
            'mail/static/src/components/chat_window/chat_window.js',
            'mail/static/src/components/chat_window_header/chat_window_header.js',
            'mail/static/src/components/chat_window_hidden_menu/chat_window_hidden_menu.js',
            'mail/static/src/components/chat_window_manager/chat_window_manager.js',
            'mail/static/src/components/chatter/chatter.js',
            'mail/static/src/components/chatter_container/chatter_container.js',
            'mail/static/src/components/chatter_topbar/chatter_topbar.js',
            'mail/static/src/components/composer/composer.js',
            'mail/static/src/components/composer_suggested_recipient/composer_suggested_recipient.js',
            'mail/static/src/components/composer_suggested_recipient_list/composer_suggested_recipient_list.js',
            'mail/static/src/components/composer_suggestion/composer_suggestion.js',
            'mail/static/src/components/composer_suggestion_list/composer_suggestion_list.js',
            'mail/static/src/components/composer_text_input/composer_text_input.js',
            'mail/static/src/components/dialog/dialog.js',
            'mail/static/src/components/dialog_manager/dialog_manager.js',
            'mail/static/src/components/discuss/discuss.js',
            'mail/static/src/components/discuss_mobile_mailbox_selection/discuss_mobile_mailbox_selection.js',
            'mail/static/src/components/discuss_sidebar/discuss_sidebar.js',
            'mail/static/src/components/discuss_sidebar_item/discuss_sidebar_item.js',
            'mail/static/src/components/drop_zone/drop_zone.js',
            'mail/static/src/components/editable_text/editable_text.js',
            'mail/static/src/components/emojis_popover/emojis_popover.js',
            'mail/static/src/components/file_uploader/file_uploader.js',
            'mail/static/src/components/follow_button/follow_button.js',
            'mail/static/src/components/follower/follower.js',
            'mail/static/src/components/follower_list_menu/follower_list_menu.js',
            'mail/static/src/components/follower_subtype/follower_subtype.js',
            'mail/static/src/components/follower_subtype_list/follower_subtype_list.js',
            'mail/static/src/components/mail_template/mail_template.js',
            'mail/static/src/components/message/message.js',
            'mail/static/src/components/message_author_prefix/message_author_prefix.js',
            'mail/static/src/components/message_list/message_list.js',
            'mail/static/src/components/message_seen_indicator/message_seen_indicator.js',
            'mail/static/src/components/messaging_menu/messaging_menu.js',
            'mail/static/src/components/mobile_messaging_navbar/mobile_messaging_navbar.js',
            'mail/static/src/components/notification_alert/notification_alert.js',
            'mail/static/src/components/notification_group/notification_group.js',
            'mail/static/src/components/notification_list/notification_list.js',
            'mail/static/src/components/notification_popover/notification_popover.js',
            'mail/static/src/components/notification_request/notification_request.js',
            'mail/static/src/components/partner_im_status_icon/partner_im_status_icon.js',
            'mail/static/src/components/thread_icon/thread_icon.js',
            'mail/static/src/components/thread_needaction_preview/thread_needaction_preview.js',
            'mail/static/src/components/thread_preview/thread_preview.js',
            'mail/static/src/components/thread_textual_typing_status/thread_textual_typing_status.js',
            'mail/static/src/components/thread_typing_icon/thread_typing_icon.js',
            'mail/static/src/components/thread_view/thread_view.js',
            'mail/static/src/model/model_core.js',
            'mail/static/src/model/model_errors.js',
            'mail/static/src/model/model_field.js',
            'mail/static/src/model/model_field_command.js',
            'mail/static/src/model/model_manager.js',
            'mail/static/src/models/activity/activity.js',
            'mail/static/src/models/activity_type/activity_type.js',
            'mail/static/src/models/attachment/attachment.js',
            'mail/static/src/models/attachment_viewer/attachment_viewer.js',
            'mail/static/src/models/canned_response/canned_response.js',
            'mail/static/src/models/channel_command/channel_command.js',
            'mail/static/src/models/chat_window/chat_window.js',
            'mail/static/src/models/chat_window_manager/chat_window_manager.js',
            'mail/static/src/models/chatter/chatter.js',
            'mail/static/src/models/composer/composer.js',
            'mail/static/src/models/country/country.js',
            'mail/static/src/models/device/device.js',
            'mail/static/src/models/dialog/dialog.js',
            'mail/static/src/models/dialog_manager/dialog_manager.js',
            'mail/static/src/models/discuss/discuss.js',
            'mail/static/src/models/follower/follower.js',
            'mail/static/src/models/follower_subtype/follower_subtype.js',
            'mail/static/src/models/follower_subtype_list/follower_subtype_list.js',
            'mail/static/src/models/locale/locale.js',
            'mail/static/src/models/mail_template/mail_template.js',
            'mail/static/src/models/message/message.js',
            'mail/static/src/models/message_seen_indicator/message_seen_indicator.js',
            'mail/static/src/models/messaging/messaging.js',
            'mail/static/src/models/messaging_initializer/messaging_initializer.js',
            'mail/static/src/models/messaging_menu/messaging_menu.js',
            'mail/static/src/models/messaging_notification_handler/messaging_notification_handler.js',
            'mail/static/src/models/model/model.js',
            'mail/static/src/models/notification/notification.js',
            'mail/static/src/models/notification_group/notification_group.js',
            'mail/static/src/models/notification_group_manager/notification_group_manager.js',
            'mail/static/src/models/partner/partner.js',
            'mail/static/src/models/suggested_recipient_info/suggested_recipient_info.js',
            'mail/static/src/models/thread/thread.js',
            'mail/static/src/models/thread_cache/thread_cache.js',
            'mail/static/src/models/thread_partner_seen_info/thread_partner_seen_info.js',
            'mail/static/src/models/thread_view/thread_view.js',
            'mail/static/src/models/thread_view/thread_viewer.js',
            'mail/static/src/models/user/user.js',
            'mail/static/src/services/chat_window_service/chat_window_service.js',
            'mail/static/src/services/dialog_service/dialog_service.js',
            'mail/static/src/services/messaging/messaging.js',
            'mail/static/src/utils/deferred/deferred.js',
            'mail/static/src/utils/throttle/throttle.js',
            'mail/static/src/utils/timer/timer.js',
            'mail/static/src/utils/utils.js',
            'mail/static/src/webclient/commands/command_category.js',
            'mail/static/src/widgets/discuss/discuss.js',
            'mail/static/src/widgets/discuss_invite_partner_dialog/discuss_invite_partner_dialog.js',
            'mail/static/src/widgets/form_renderer/form_renderer.js',
            'mail/static/src/widgets/messaging_menu/messaging_menu.js',
            'mail/static/src/widgets/notification_alert/notification_alert.js',
            'mail/static/src/components/notification_list/notification_list_item.scss',
            'mail/static/src/components/activity/activity.scss',
            'mail/static/src/components/activity_box/activity_box.scss',
            'mail/static/src/components/activity_mark_done_popover/activity_mark_done_popover.scss',
            'mail/static/src/components/attachment/attachment.scss',
            'mail/static/src/components/attachment_box/attachment_box.scss',
            'mail/static/src/components/attachment_list/attachment_list.scss',
            'mail/static/src/components/attachment_viewer/attachment_viewer.scss',
            'mail/static/src/components/chat_window/chat_window.scss',
            'mail/static/src/components/chat_window_header/chat_window_header.scss',
            'mail/static/src/components/chat_window_hidden_menu/chat_window_hidden_menu.scss',
            'mail/static/src/components/chat_window_manager/chat_window_manager.scss',
            'mail/static/src/components/chatter/chatter.scss',
            'mail/static/src/components/chatter_container/chatter_container.scss',
            'mail/static/src/components/chatter_topbar/chatter_topbar.scss',
            'mail/static/src/components/composer/composer.scss',
            'mail/static/src/components/composer_suggested_recipient/composer_suggested_recipient.scss',
            'mail/static/src/components/composer_suggested_recipient_list/composer_suggested_recipient_list.scss',
            'mail/static/src/components/composer_suggestion/composer_suggestion.scss',
            'mail/static/src/components/composer_suggestion_list/composer_suggestion_list.scss',
            'mail/static/src/components/composer_text_input/composer_text_input.scss',
            'mail/static/src/components/dialog/dialog.scss',
            'mail/static/src/components/discuss/discuss.scss',
            'mail/static/src/components/discuss_mobile_mailbox_selection/discuss_mobile_mailbox_selection.scss',
            'mail/static/src/components/discuss_sidebar/discuss_sidebar.scss',
            'mail/static/src/components/discuss_sidebar_item/discuss_sidebar_item.scss',
            'mail/static/src/components/drop_zone/drop_zone.scss',
            'mail/static/src/components/emojis_popover/emojis_popover.scss',
            'mail/static/src/components/file_uploader/file_uploader.scss',
            'mail/static/src/components/follow_button/follow_button.scss',
            'mail/static/src/components/follower/follower.scss',
            'mail/static/src/components/follower_list_menu/follower_list_menu.scss',
            'mail/static/src/components/follower_subtype/follower_subtype.scss',
            'mail/static/src/components/follower_subtype_list/follower_subtype_list.scss',
            'mail/static/src/components/mail_template/mail_template.scss',
            'mail/static/src/components/message/message.scss',
            'mail/static/src/components/message_author_prefix/message_author_prefix.scss',
            'mail/static/src/components/message_list/message_list.scss',
            'mail/static/src/components/message_seen_indicator/message_seen_indicator.scss',
            'mail/static/src/components/messaging_menu/messaging_menu.scss',
            'mail/static/src/components/mobile_messaging_navbar/mobile_messaging_navbar.scss',
            'mail/static/src/components/notification_group/notification_group.scss',
            'mail/static/src/components/notification_list/notification_list.scss',
            'mail/static/src/components/notification_popover/notification_popover.scss',
            'mail/static/src/components/notification_request/notification_request.scss',
            'mail/static/src/components/partner_im_status_icon/partner_im_status_icon.scss',
            'mail/static/src/components/thread_icon/thread_icon.scss',
            'mail/static/src/components/thread_needaction_preview/thread_needaction_preview.scss',
            'mail/static/src/components/thread_preview/thread_preview.scss',
            'mail/static/src/components/thread_textual_typing_status/thread_textual_typing_status.scss',
            'mail/static/src/components/thread_typing_icon/thread_typing_icon.scss',
            'mail/static/src/components/thread_view/thread_view.scss',
            'mail/static/src/widgets/discuss/discuss.scss',
            'mail/static/src/widgets/form_renderer/form_renderer.scss',
        ],
        'web.assets_backend_prod_only': [
            'mail/static/src/js/main.js',
        ],
        'web.assets_tests': [
            'mail/static/tests/tours/**/*',
        ],
        'web.tests_assets': [
            'mail/static/src/env/test_env.js',
            'mail/static/src/utils/test_utils.js',
            'mail/static/tests/helpers/mock_models.js',
            'mail/static/tests/helpers/mock_server.js',
        ],
        'web.qunit_suite_tests': [
            'mail/static/tests/chatter_tests.js',
            'mail/static/tests/mail_utils_tests.js',
            'mail/static/tests/document_viewer_tests.js',
            'mail/static/tests/m2x_avatar_user_tests.js',
            'mail/static/tests/systray/systray_activity_menu_tests.js',
            'mail/static/tests/tools/debug_manager_tests.js',
            'mail/static/tests/activity_tests.js',
            'mail/static/src/component_hooks/use_store/use_store_tests.js',
            'mail/static/src/components/activity/activity_tests.js',
            'mail/static/src/components/activity_mark_done_popover/activity_mark_done_popover_tests.js',
            'mail/static/src/components/attachment/attachment_tests.js',
            'mail/static/src/components/attachment_box/attachment_box_tests.js',
            'mail/static/src/components/chat_window_manager/chat_window_manager_tests.js',
            'mail/static/src/components/chatter/chatter_tests.js',
            'mail/static/src/components/chatter/chatter_suggested_recipient_tests.js',
            'mail/static/src/components/chatter_topbar/chatter_topbar_tests.js',
            'mail/static/src/components/composer/composer_tests.js',
            'mail/static/src/components/composer_suggestion/composer_suggestion_canned_response_tests.js',
            'mail/static/src/components/composer_suggestion/composer_suggestion_channel_tests.js',
            'mail/static/src/components/composer_suggestion/composer_suggestion_command_tests.js',
            'mail/static/src/components/composer_suggestion/composer_suggestion_partner_tests.js',
            'mail/static/src/components/dialog_manager/dialog_manager_tests.js',
            'mail/static/src/components/discuss/tests/discuss_inbox_tests.js',
            'mail/static/src/components/discuss/tests/discuss_pinned_tests.js',
            'mail/static/src/components/discuss/tests/discuss_sidebar_tests.js',
            'mail/static/src/components/discuss/tests/discuss_tests.js',
            'mail/static/src/components/file_uploader/file_uploader_tests.js',
            'mail/static/src/components/follow_button/follow_button_tests.js',
            'mail/static/src/components/follower/follower_tests.js',
            'mail/static/src/components/follower_list_menu/follower_list_menu_tests.js',
            'mail/static/src/components/follower_subtype/follower_subtype_tests.js',
            'mail/static/src/components/message/message_tests.js',
            'mail/static/src/components/message_seen_indicator/message_seen_indicator_tests.js',
            'mail/static/src/components/messaging_menu/messaging_menu_tests.js',
            'mail/static/src/components/notification_list/notification_list_notification_group_tests.js',
            'mail/static/src/components/notification_list/notification_list_tests.js',
            'mail/static/src/components/partner_im_status_icon/partner_im_status_icon_tests.js',
            'mail/static/src/components/thread_icon/thread_icon_tests.js',
            'mail/static/src/components/thread_needaction_preview/thread_needaction_preview_tests.js',
            'mail/static/src/components/thread_preview/thread_preview_tests.js',
            'mail/static/src/components/thread_textual_typing_status/thread_textual_typing_status_tests.js',
            'mail/static/src/components/thread_view/thread_view_tests.js',
            'mail/static/src/model/tests/test_models.js',
            'mail/static/src/model/tests/model_field_command/clear_tests.js',
            'mail/static/src/model/tests/model_field_command/create_tests.js',
            'mail/static/src/model/tests/model_field_command/insert_and_replace_tests.js',
            'mail/static/src/model/tests/model_field_command/insert_tests.js',
            'mail/static/src/model/tests/model_field_command/link_tests.js',
            'mail/static/src/model/tests/model_field_command/replace_tests.js',
            'mail/static/src/model/tests/model_field_command/set_tests.js',
            'mail/static/src/model/tests/model_field_command/unlink_all_tests.js',
            'mail/static/src/model/tests/model_field_command/unlink_tests.js',
            'mail/static/src/models/attachment/attachment_tests.js',
            'mail/static/src/models/message/message_tests.js',
            'mail/static/src/models/messaging/messaging_tests.js',
            'mail/static/src/models/thread/thread_tests.js',
            'mail/static/src/utils/throttle/throttle_tests.js',
            'mail/static/src/utils/timer/timer_tests.js',
            'mail/static/src/widgets/form_renderer/form_renderer_tests.js',
            'mail/static/src/widgets/notification_alert/notification_alert_tests.js',
        ],
        'web.qunit_mobile_suite_tests': [
            'mail/static/src/components/discuss_mobile_mailbox_selection/discuss_mobile_mailbox_selection_tests.js',
        ],
        'web.assets_qweb': [
            'mail/static/src/xml/activity.xml',
            'mail/static/src/xml/activity_view.xml',
            'mail/static/src/xml/composer.xml',
            'mail/static/src/xml/many2one_avatar_user.xml',
            'mail/static/src/xml/systray.xml',
            'mail/static/src/xml/thread.xml',
            'mail/static/src/xml/web_kanban_activity.xml',
            'mail/static/src/xml/text_emojis.xml',
            'mail/static/src/components/activity/activity.xml',
            'mail/static/src/components/activity_box/activity_box.xml',
            'mail/static/src/components/activity_mark_done_popover/activity_mark_done_popover.xml',
            'mail/static/src/components/attachment/attachment.xml',
            'mail/static/src/components/attachment_box/attachment_box.xml',
            'mail/static/src/components/attachment_delete_confirm_dialog/attachment_delete_confirm_dialog.xml',
            'mail/static/src/components/attachment_list/attachment_list.xml',
            'mail/static/src/components/attachment_viewer/attachment_viewer.xml',
            'mail/static/src/components/autocomplete_input/autocomplete_input.xml',
            'mail/static/src/components/chat_window/chat_window.xml',
            'mail/static/src/components/chat_window_header/chat_window_header.xml',
            'mail/static/src/components/chat_window_hidden_menu/chat_window_hidden_menu.xml',
            'mail/static/src/components/chat_window_manager/chat_window_manager.xml',
            'mail/static/src/components/chatter/chatter.xml',
            'mail/static/src/components/chatter_container/chatter_container.xml',
            'mail/static/src/components/chatter_topbar/chatter_topbar.xml',
            'mail/static/src/components/composer/composer.xml',
            'mail/static/src/components/composer_suggested_recipient/composer_suggested_recipient.xml',
            'mail/static/src/components/composer_suggested_recipient_list/composer_suggested_recipient_list.xml',
            'mail/static/src/components/composer_suggestion/composer_suggestion.xml',
            'mail/static/src/components/composer_suggestion_list/composer_suggestion_list.xml',
            'mail/static/src/components/composer_text_input/composer_text_input.xml',
            'mail/static/src/components/dialog/dialog.xml',
            'mail/static/src/components/dialog_manager/dialog_manager.xml',
            'mail/static/src/components/discuss/discuss.xml',
            'mail/static/src/components/discuss_mobile_mailbox_selection/discuss_mobile_mailbox_selection.xml',
            'mail/static/src/components/discuss_sidebar/discuss_sidebar.xml',
            'mail/static/src/components/discuss_sidebar_item/discuss_sidebar_item.xml',
            'mail/static/src/components/drop_zone/drop_zone.xml',
            'mail/static/src/components/editable_text/editable_text.xml',
            'mail/static/src/components/emojis_popover/emojis_popover.xml',
            'mail/static/src/components/file_uploader/file_uploader.xml',
            'mail/static/src/components/follow_button/follow_button.xml',
            'mail/static/src/components/follower/follower.xml',
            'mail/static/src/components/follower_list_menu/follower_list_menu.xml',
            'mail/static/src/components/follower_subtype/follower_subtype.xml',
            'mail/static/src/components/follower_subtype_list/follower_subtype_list.xml',
            'mail/static/src/components/mail_template/mail_template.xml',
            'mail/static/src/components/message/message.xml',
            'mail/static/src/components/message_author_prefix/message_author_prefix.xml',
            'mail/static/src/components/message_list/message_list.xml',
            'mail/static/src/components/message_seen_indicator/message_seen_indicator.xml',
            'mail/static/src/components/messaging_menu/messaging_menu.xml',
            'mail/static/src/components/mobile_messaging_navbar/mobile_messaging_navbar.xml',
            'mail/static/src/components/notification_alert/notification_alert.xml',
            'mail/static/src/components/notification_group/notification_group.xml',
            'mail/static/src/components/notification_list/notification_list.xml',
            'mail/static/src/components/notification_popover/notification_popover.xml',
            'mail/static/src/components/notification_request/notification_request.xml',
            'mail/static/src/components/partner_im_status_icon/partner_im_status_icon.xml',
            'mail/static/src/components/thread_icon/thread_icon.xml',
            'mail/static/src/components/thread_needaction_preview/thread_needaction_preview.xml',
            'mail/static/src/components/thread_preview/thread_preview.xml',
            'mail/static/src/components/thread_textual_typing_status/thread_textual_typing_status.xml',
            'mail/static/src/components/thread_typing_icon/thread_typing_icon.xml',
            'mail/static/src/components/thread_view/thread_view.xml',
            'mail/static/src/widgets/common.xml',
            'mail/static/src/widgets/discuss/discuss.xml',
            'mail/static/src/widgets/discuss_invite_partner_dialog/discuss_invite_partner_dialog.xml',
            'mail/static/src/widgets/messaging_menu/messaging_menu.xml',
        ],
    }
}
