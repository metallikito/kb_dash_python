def create_banner(project_name):
    base_banner = "ndjson banner"  # use _export method from saved_objects API to get base banner
    new_banner = "ndjson banner edited"  # edit ndjson to change the title with project_name
    banner_id = "uuid returned from _import method"  # use _import method from saved_objects API to create a new banner
    return banner_id


def create_visualization(project_name):
    base_visualization = "ndjson visualization"  # use _export method from saved_objects API to get base banner
    new_visualization = "ndjson banner edited"  # edit ndjson to change the title with project_name
    visualization_id = "uuid returned from _import method"  # use _import method from saved_objects API to create a new banner
    return visualization_id