/** @odoo-module **/

import { onWillStart, useState } from "@odoo/owl";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { NavBar } from "@web/webclient/navbar/navbar";

patch(NavBar.prototype, {
    setup() {
        super.setup(...arguments);
        this.quickSwitcherOrm = useService("orm");
        this.quickSwitcherState = useState({ menuIds: [] });

        onWillStart(async () => {
            this.quickSwitcherState.menuIds = await this.quickSwitcherOrm.call(
                "res.users",
                "get_quick_app_menu_ids",
                []
            );
        });
    },

    get quickSwitcherShortcuts() {
        const selectedMenuIds = new Set(this.quickSwitcherState.menuIds.map(Number));
        return this.menuService
            .getApps()
            .filter((app) => selectedMenuIds.has(Number(app.id)));
    },

    async onQuickSwitcherSelect(app) {
        await this.menuService.selectMenu(app);
    },
});
