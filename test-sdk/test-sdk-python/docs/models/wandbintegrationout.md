# WandbIntegrationOut


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `project`                                                                        | *str*                                                                            | :heavy_check_mark:                                                               | The name of the project that the new run will be created under.                  |
| `type`                                                                           | [Optional[models.WandbIntegrationOutType]](../models/wandbintegrationouttype.md) | :heavy_minus_sign:                                                               | N/A                                                                              |
| `name`                                                                           | *OptionalNullable[str]*                                                          | :heavy_minus_sign:                                                               | A display name to set for the run. If not set, will use the job ID as the name.  |
| `run_name`                                                                       | *OptionalNullable[str]*                                                          | :heavy_minus_sign:                                                               | N/A                                                                              |