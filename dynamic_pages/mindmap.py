import streamlit as st
import streamlit_mermaid


@st.cache_data
def small_mindmap():

    code = """
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#91b6e2','secondaryColor':'#a0d5a0','tertiaryColor':'#e5a1d2','quaternaryColor':'#f2e085','textColor':'#2b2b2b','fontFamily':'Arial, sans-serif','noteBkgColor':'#fcf4dd'}}}%%

mindmap
    Root((Flat Knowledge Base))
        aws
        bash
        business and personal
        cloud
        code review
        coding patterns
        data engineering
        databricks
        django
        fastapi
        fastapi profiling tools
        flask
        git
        join
        kafka
        keras
        kubernetes
        languages
        lime
        linux kernel
        llm
        math
        matplotlib pyplot
        message brokers
        metrics
        ml flow
        nano
        numpy
        pandas
        poetry
        power bi
        principles
        pydantic
        pyspark
        python
        pytorch
        rag retrieval augmented generation
        scipy
        seaborn
        shap
        sklearn
        software engineering
        sql
        stream protocols
        tensorflow
        terraform
"""
    return code


def st_mindmap():
    code = """
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#91b6e2','secondaryColor':'#a0d5a0','tertiaryColor':'#e5a1d2','quaternaryColor':'#f2e085','textColor':'#2b2b2b','fontFamily':'Arial, sans-serif','noteBkgColor':'#fcf4dd'}}}%%
    
mindmap
  root((Knowledge Base))
    aws
        cloud development kit
        services
    bash
    business and personal
        added value
        advocate
        pricing strategies
        business impact
        supply chain
        added value
        impact
        economic models
        creativity
        mba
        presentation
        pricing strategies
    cloud
        aws devops
        aws service list
        azure devops
        azure service list
        cloud based ml system design
        gcp service list
    code review
    coding patterns
        algorithms
        coding patterns
        python
    data engineering
        data engineer
        data engineer concepts
        data engineering layers
        design data pipelines
        etl
        etl duplicate
        etl final
        ha fault tolerant
        knowledge and tools
        lambda vs kappa
        optimize pipelines
        optimize slow query
        pipeline
        pipeline data quality
        pipeline failures
        pyspark
        real time pipeline
        schema evolution
        skills data engineer
        unstructured data
    databricks
        azure databricks
        databricks
        databricks api
        databricks aws
        databricks inbound
        databricks ui
    django
    fastapi
    fastapi profiling tools
    flask
    git
    join
    kafka
        kafka
        kafka inbound
        kafka stream and db
    keras
    kubernetes
    languages
        cpp
        ruby
    lime
    linux kernel
    llm
        perplexity and anthropic
        vector database
    math
        calculus
        distributions
        regression coefficient
        statistics
    matplotlib pyplot
    message brokers
    metrics
    ml flow
        ml flow short summary
        ml flow sklearn regression example
    nano
    numpy
        numpy
        numpy axis
        numpy examples
        numpy queries
    pandas
        pandas
        pandas axis
        pandas examples
        pandas function list
        pandas merge
        pandas ml related
        pandas pivot and reset index
        pandas queries
        pandas shapes
        pandas vocabulary
    poetry
    power bi
    principles
        acid
        clean code
        design patterns
        functional programming
        getting things done
        ingest scoring
        oop principles
        oop principles in Hungarian
        software architecture principles
        solid
        syntactic sugars
    pydantic
    pyspark
        pyspark
        pyspark bucketing vs partitioning
        pyspark dataframe
        pyspark etl
        pyspark inbound
        pyspark linear regression optimization
        pyspark linear regression workflow
        pyspark ml classification
        pyspark ml classification gradient boosted trees
        pyspark ml classification random forest
        pyspark ml clustering
        pyspark ml evaluation
        pyspark ml evaluation auc
        pyspark ml evaluation evaluators
        pyspark ml feature hashing tf
        pyspark ml feature idf
        pyspark ml feature one hot encoder
        pyspark ml feature stop words remover
        pyspark ml feature string indexer
        pyspark ml feature tokenizer
        pyspark ml feature vector assembler
        pyspark ml linear regression pipeline
        pyspark ml recommendation als
        pyspark ml recommendation als example
        pyspark ml regression
        pyspark ml tuning cross validator
        pyspark ml tuning grid search
        pyspark mllib
        pyspark model save
        pyspark shuffle
        pyspark some modules
        pyspark sql
        pyspark sql functions monotonically increasing id
        pyspark structured streaming
        pyspark time series basic
        pyspark vocabulary
    python
        pyenv
        python
        python coding standards
        python more
        python packages
        python slicing
    pytorch
    rag retrieval augmented generation
    scipy
        scipy stats binom
        scipy stats norm
        scipy stats poisson
        scipy stats uniform
    seaborn
    shap
    sklearn
        scikit learn
        scikit learn real estate price prediction example
    software engineering
        async
        debug
        design
        gil
        knowledge and tools
        large scale software development
        logging design
        memory
        microservices architecture
        optimize slow code
        restful api design
        skills software engineer
        software application design
        software development design patterns
        software engineer
        write concurrent db
    sql
        sql
        sql alchemy
        sql clause order
        sql conversations create queries
        sql conversations samle data
        sql cte
        sql example
        sql index
        sql new
        sql small schema
        sql vocabulary
        sql while
        sql window
    stream protocols
        grpc
        grps vs websockets
    tensorflow
    terraform
"""
    
    streamlit_mermaid.st_mermaid(code)
