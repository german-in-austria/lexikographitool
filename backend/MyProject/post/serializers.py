from rest_framework import serializers

from .models import Post, Report
from account.serializers import UserNameSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserNameSerializer()
    is_author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'parent', 'author', 'children','is_author','date_created', 'edited']



    def get_is_author(self,post):
        if 'request' not in self.context:
            return False
        return post.author == self.context['request'].user


class PostSimpleSerializer(serializers.ModelSerializer):
    author = UserNameSerializer()

    class Meta:
        model = Post
        fields = ['id', 'text', 'author']

class PostCreateSerializer(serializers.ModelSerializer):
    author = UserNameSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'text', 'parent', 'author', 'lexeme']
class ReportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    report_from = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Report
        fields = '__all__'

    def get_report_from(self, report):
        return report.report_from.username