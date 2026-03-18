import factory

from app.agents.services.analytics_service import PostMetricsSummary
from app.agents.services.content_service import ContentBrief


class ContentBriefFactory(factory.Factory):
    class Meta:
        model = ContentBrief

    topic = factory.Sequence(lambda n: f"Art topic {n}")
    platform = "instagram"
    tone = "authentic"
    brand_voice = None
    constraints = None


class PostMetricsSummaryFactory(factory.Factory):
    class Meta:
        model = PostMetricsSummary

    post_id = factory.Sequence(lambda n: f"post-{n}")
    platform = "instagram"
    impressions = 1000
    reach = 800
    likes = 50
    comments = 10
    shares = 5
    engagement_rate = 6.5
