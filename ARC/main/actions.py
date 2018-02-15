import re
from main.models import CDC, CourseSlot, Output


def single_option_CDC(modeladmin, request, queryset):
    for student in queryset:
        branches = get_branch(student.CAMPUS_ID)
        year = 2
        sem = 2

        for branch in branches:
            CDCs = get_cdcs(branch, year, sem)
            for cdc in CDCs:
                print(cdc.comp_codes)
                if check_if_single_option_CDC(cdc.comp_codes):
                    generate_output(cdc.comp_codes, student, cdc)


single_option_CDC.short_description = "Generate single option CDC data."


def get_branch(CAMPUS_ID):
    branches = []
    for i in [CAMPUS_ID[4:6], CAMPUS_ID[6:8]]:
        if i[0] == "A" or i[0] == "B":
            branches.append(i)
    return branches


def get_cdcs(branch, year, sem):
    return CDC.objects.filter(
        tag=branch + "CDC").filter(year=year).filter(sem=sem)


def check_if_single_option_CDC(comp_codes):

    # logic to check if single option
    # course_slots = get_course_slots(comp_codes)

    nP = len(CourseSlot.objects.filter(
        course_id__endswith=comp_codes).filter(section__startswith="P"))
    nL = len(CourseSlot.objects.filter(
        course_id__endswith=comp_codes).filter(section__startswith="L"))
    nG = len(CourseSlot.objects.filter(
        course_id__endswith=comp_codes).filter(section__startswith="G"))

    print(nP, nL, nG)
    if nP <= 1 and nL <= 1 and nG <= 1:
        return True

    return False


def get_course_slots(comp_codes):

    return CourseSlot.objects.filter(course_id__endswith=comp_codes)


def generate_output(comp_codes, student, cdc):
    print(cdc)  # , comp_codes, cdc)
    courseslots = get_course_slots(comp_codes)
    print(courseslots)
    for slot in courseslots:
        print(slot)
        output = Output(EMPLID=student.id,
                        CAMPUS_ID=student.CAMPUS_ID,
                        CRSE_ID=int(cdc.comp_codes),
                        SUBJECT=re.split('\W+', cdc.course_code)[0],
                        CATALOG_NBR=re.split('\W+', cdc.course_code)[1],
                        DESCR=cdc.course_name,
                        CLASS_NBR=int(float(slot.class_nbr)),
                        CLASS_SECTION=slot.section)
        output.save()
