# CheckpointOut


## Fields

| Field                                                                                                                                                                        | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  | Example                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `metrics`                                                                                                                                                                    | [models.MetricOut](../models/metricout.md)                                                                                                                                   | :heavy_check_mark:                                                                                                                                                           | Metrics at the step number during the fine-tuning job. Use these metrics to assess if the training is going smoothly (loss should decrease, token accuracy should increase). |                                                                                                                                                                              |
| `step_number`                                                                                                                                                                | *int*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | The step number that the checkpoint was created at.                                                                                                                          |                                                                                                                                                                              |
| `created_at`                                                                                                                                                                 | *int*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | The UNIX timestamp (in seconds) for when the checkpoint was created.                                                                                                         | 1716963433                                                                                                                                                                   |