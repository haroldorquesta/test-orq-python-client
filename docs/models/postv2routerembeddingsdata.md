# PostV2RouterEmbeddingsData


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `object`                                                                                     | [models.PostV2RouterEmbeddingsRouterObject](../models/postv2routerembeddingsrouterobject.md) | :heavy_check_mark:                                                                           | The object type, which is always "embedding".                                                |
| `embedding`                                                                                  | [models.Embedding](../models/embedding.md)                                                   | :heavy_check_mark:                                                                           | The embedding result.                                                                        |
| `index`                                                                                      | *float*                                                                                      | :heavy_check_mark:                                                                           | The index of the embedding in the list of embeddings.                                        |