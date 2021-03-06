from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Student, CDC, CourseSlot, Output


# from .utils import TimeWidget, DateWidget, CompCodesWidget


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        import_id_fields = ['id']
        fields = ['id', 'CAMPUS_ID', 'NAME', 'YEAR', 'DISC']


class CDCResource(resources.ModelResource):
    class Meta:
        model = CDC
        import_id_fields = ['comp_codes']
        fields = [
            'comp_codes',
            'course_code',
            'tag',
            'course_name',
            'units',
            'year',
            'sem'
        ]
        exclude = ('id', )


class OutputResource(resources.ModelResource):
    class Meta:
        model = Output

        exclude = ('id', )


class CourseSlotResource(resources.ModelResource):

    class Meta:
        model = CourseSlot

        import_id_fields = ['class_nbr']
        fields = [
            'course_id',
            'class_nbr',
            'section', ]
        # 'CDC__comp_codes',
        # 'course',
        # 'room',
        # 'class_pattern',
        # 'mtg_start',
        # 'end_time',
        # 'instructor_ID',
        # 'instructor_name',
        # 'instructor_role',
        # 'exam_tm_cd',
        # # 'exam_date',
        # 'course_admin',

    # mtg_start = fields.Field(
    #     column_name="mtg_start",
    #     widget=TimeWidget(),
    # )

    # end_time = fields.Field(
    #     column_name="end_time",
    #     widget=TimeWidget(),
    # )

    # exam_date = fields.Field(
    #     column_name="exam_date",
    #     widget=DateWidget(),
    # )

    # def skip_row(self, instance, original):
    #     """
    #     Returns ``True`` if ``row`` importing should be skipped.
    #     """
    #     print("Enter")
    #     if not self._meta.skip_unchanged:
    #         # print("enter2")
    #         return False
    #     for field in self.get_import_fields():
    #         print(field.column_name)
    #         try:
    #             # For fields that are models.fields.related.ManyRelatedManager
    #             # we need to compare the results
    #             if list(field.get_value(instance).all()) != list(field.get_value(original).all()):
    #                 return False
    #         except AttributeError:
    #             if field.get_value(instance) != field.get_value(original):
    #                 return False
    #         if field.column_name == "course_id":# and field.get_value(instance)==None:
    #             print("############",field.get_value(instance))
    #             print("YAY")
    #             return False

    #     return True
