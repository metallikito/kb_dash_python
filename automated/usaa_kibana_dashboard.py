import usaa_kibana_visualization

class KibanaDashboardProcessor:
    def __init__(self):
        self.foo = "foo"

    def find_dashboard_by_group(self, group):
        dashboard_id = "uuid"  # use _find method from saved_objects API to get the id
        return dashboard_id

    def get_dashboard(self, group):
        dashboard_id = self.find_dashboard_by_group(group)
        if dashboard_id:
            dashboard = "ndjson from _export"  # use _export method from saved_objects API to read dashboard with this id
            return {
                "is_default": False,
                "dashboard": dashboard
            }
        else:
            dashboard = "ndjson from default"  # use static file in this project or read the base dashboard from Kibana
            return {
                "is_default": True,
                "dashboard": dashboard
            }

    def add_group_components(self, dashboard, banner, visualization):
        dashboard_with_new_components = "ndjson with new lines for banner and visualization"  # plus change panelsJSON
        # property and references property in tha last line, to add the position and the references to the ID of
        # banner and visualization
        return dashboard_with_new_components


    def process(self, **kwargs):
        group = kwargs.get("group")  # check how to get from pipeline/job context execution
        project_name = kwargs.get("project")  # check how to get from pipeline/job context execution
        dashboard = self.get_dashboard(group)
        new_banner = usaa_kibana_visualization.create_banner(project_name)
        new_visualization = usaa_kibana_visualization.create_visualization(project_name)
        edited_dashboard = self.add_group_components(dashboard, new_banner, new_visualization)
        #  import to Kibana with _import method, do not override

        return None

