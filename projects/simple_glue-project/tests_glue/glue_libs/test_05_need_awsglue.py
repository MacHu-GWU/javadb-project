# -*- coding: utf-8 -*-

"""
This example depends on awsglue lib, pyspark, 3rd party python library
and your custom python library.
"""

from pyspark.context import SparkContext
from pyspark.sql import DataFrame

from awsglue import DynamicFrame
from awsglue.context import GlueContext

from simple_glue.glue_libs.glue_utils import double_a_column


def test():
    spark_ctx = SparkContext.getOrCreate()
    glue_ctx = GlueContext(spark_ctx)
    spark_ses = glue_ctx.spark_session

    pdf: DataFrame = spark_ses.createDataFrame(
        [
            ("a", 1),
            ("b", 2),
            ("c", 3),
        ],
        ("id", "value"),
    )
    gdf: DynamicFrame = DynamicFrame.fromDF(pdf, glue_ctx, "gdf")

    gdf1 = double_a_column(gdf, "value", "gdf1")
    pdf1 = gdf1.toDF()
    assert list(pdf1.select("value").toPandas()["value"]) == [2, 4, 6]
    print("")
    pdf1.show()


if __name__ == "__main__":
    from simple_glue.tests.glue import run_unit_test

    run_unit_test(__file__, glue_version="4.0")
