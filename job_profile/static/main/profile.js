"use strict";

$(function() {
    $("#link-add-id").click(function(){
    	var input_num = parseInt($("input[name='form_num']").val());
    	input_num = input_num + 1;
    	$("input[name='form_num']").val(''+input_num+'');

        var content = '<div class="row form-item">' +
            '<div class="col-md-5 mb-3">' +
                '<label class="form-label">Link Name</label>' +
                '<input type="text" class="form-control" name="name-link_'+input_num+'">' +
            '</div>' +
            '<div class="col-md-5 mb-3">' +
                '<label class="form-label">Link Url</label>' +
                '<input type="text" class="form-control" name="link-link_'+input_num+'">' +
            '</div>' +
            '<div class="col-md-2">' +
                '<a class="btn btn-danger trash" href="javascript:void(0);">DELETE</a>' +
            '</div>' +
        '</div>';
    	
        $(".form-row").append(content);
        return false;
    });


    $("#edu-add-id").click(function(){
    	var input_num = parseInt($("input[name='form_num']").val());
        input_num = input_num + 1;
        $("input[name='form_num']").val(''+input_num+'');

    	var listcontent = '<div class="row form-item pt-4">' +
            '<div class="col-md-6 mb-3">' +
                '<label>Institution</label>' +
                '<input type="text" class="form-control" name="institution-edu_'+input_num+'">' +
            '</div>' +
            '<div class="col-md-6 mb-3">' +
                '<label>Location</label>' +
                '<input type="text" class="form-control" name="location-edu_'+input_num+'">' +
            '</div>' +
            '<div class="col-md-6 mb-3">' +
                '<label>Study Area</label>' +
                '<input type="text" class="form-control" name="study_area-edu_'+input_num+'" placeholder="Eg. Bachelor of Science">' +
            '</div>' +
            '<div class="col-md-6 mb-3">' +
                '<label>Study Type</label>' +
                '<input type="text" class="form-control" name="study_type-edu_'+input_num+'" placeholder="Eg. Computer Science">' +
            '</div>' +
            '<div class="col-md-6 mb-3">' +
                    '<label>Start Date</label>' +
                    '<input type="text" class="form-control datepicker" name="start_date-edu_'+input_num+'" placeholder="YYYY-MM-DD">' +
            '</div>' +
            '<div class="col-md-6 mb-3">' +
                    '<label>End Date</label>' +
                    '<input type="text" class="form-control datepicker" name="end_date-edu_'+input_num+'" placeholder="YYYY-MM-DD">' +
            '</div>' +
            '<div class="col-md-6 mb-3">' +
                    '<label>GPA</label>' +
                    '<input type="text" class="form-control" name="gpa-edu_'+input_num+'">' +
            '</div>' + 
        '</div>';

        $(".form-row").append(listcontent);
        return false;
    });


    $("#work-add-id").click(function(){
        var input_num = parseInt($("input[name='form_num']").val());
        input_num = input_num + 1;
        $("input[name='form_num']").val(''+input_num+'');

        var listcontent = '<div class="row form-item pt-4">' +
            '<div class="col-md-6 mb-3">' +
                '<label>Company</label>' +
                '<input type="text" class="form-control" name="company-work_'+input_num+'">' +
            '</div>' +
            '<div class="col-md-6 mb-3">' +
                '<label>Location</label>' +
                '<input type="text" class="form-control" name="location-work_'+input_num+'">' +
            '</div>' +
            '<div class="col-md-6 mb-3">' +
                '<label>Position</label>' +
                '<input type="text" class="form-control" name="position-work_'+input_num+'">' +
            '</div>' +
            '<div class="col-md-6 mb-3">' +
                '<label>Website</label>' +
                '<input type="text" class="form-control" name="website-work_'+input_num+'">' +
            '</div>' +

            '<div class="col-md-6 mb-3">' +
                '<label>Start Date</label>' +
                '<input type="text" class="form-control datepicker" name="start_date-work_'+input_num+'" placeholder="YYYY-MM-DD">' +
            '</div>' +
            '<div class="col-md-6 mb-3">' +
                '<label>End Date</label>' +
                '<input type="text" class="form-control datepicker" name="end_date-work_'+input_num+'" placeholder="YYYY-MM-DD">' +
            '</div>' +
        '</div>'; 

        $(".form-row").append(listcontent);
        return false;
    });

    $("#skill-add-id").click(function(){
        var input_num = parseInt($("input[name='form_num']").val());
        input_num = input_num + 1;
        $("input[name='form_num']").val(''+input_num+'');

        var listcontent = '<div class="row form-item">' +
            '<div class="col-md-4 mb-3">' +
                '<label class="form-label">Skill Name</label>' +
                '<input type="text" class="form-control" name="name-skill_'+input_num+'" placeholder="Eg. Frontend" required>' +
            '</div>' +
            '<div class="col-md-6 mb-3">' +
                '<label class="form-label">Skill Keywords</label>' +
                '<input type="text" class="form-control" name="keywords-skill_'+input_num+'" placeholder="Eg. HTML, XML, CSS, Bootsrap" required>' +
            '</div>' +
            '<div class="col-md-2 mb-3">' +
                '<a class="btn btn-danger" href="javascript:void(0);">DELETE</a>' +
            '</div>' +        
        '</div>';

        $(".form-row").append(listcontent);
        return false;
    });

    $("#project-add-id").click(function(){
        var input_num = parseInt($("input[name='form_num']").val());
        input_num = input_num + 1;
        $("input[name='form_num']").val(''+input_num+'');

        var listcontent = '<div class="row form-item pt-4">' +
            '<div class="col-md-6 mb-3">' +
                '<label class="form-label">Project Name</label>' +
                '<input type="text" class="form-control" name="name-project_'+input_num+'" required>' +
            '</div>' + 
            '<div class="col-md-6 mb-3">' +
                '<label>Link</label>' +
                '<input type="text" class="form-control" name="url-project_'+input_num+'">' +
            '</div>' + 
            '<div class="col-md-6 mb-3">' +
                '<label class="form-label">Date</label>' +
                '<input type="text" class="form-control" name="date-project_'+input_num+'" placeholder="Formart: YYYY-MM-DD" required>' +
            '</div>' +
            '<div class="col-md-6 mb-3">' +
                '<label class="form-label">Project Technologies</label>' +
                '<input type="text" class="form-control" name="technologies-project_'+input_num+'" placeholder="Eg: Python, Flutter, XML, CSS">' +
            '</div>' +
            '<div class="col-md-6 mb-3">' +
                '<label>Description</label>' +
                '<textarea class="form-control" name="description-project_'+input_num+'" rows="5"></textarea>' +
            '</div>' + 
        '</div>';

        $(".form-row").append(listcontent);
        return false;
    });

    $("#award-add-id").click(function(){
        var input_num = parseInt($("input[name='form_num']").val());
        input_num = input_num + 1;
        $("input[name='form_num']").val(''+input_num+'');

        var listcontent = '<div class="row form-item pt-4">' +
            '<div class="col-md-6 mb-3">' +
                '<label>Title</label>' +
                '<input type="text" class="form-control" name="title-award_'+input_num+'">' +
            '</div>' + 
            '<div class="col-md-6 mb-3">' +
                '<label>Date</label>' +
                '<input type="text" class="form-control datepicker" name="date-award_'+input_num+'" placeholder="YYYY-MM-DD">' +
            '</div>' +
            '<div class="col-md-6 mb-3">' +
                '<label>Awarder</label>' +
                '<input type="text" class="form-control" name="awarder-award_'+input_num+'">' +
            '</div>' +
            '<div class="col-md-6 mb-3">' +
                '<label>Summary</label>' +
                '<textarea class="form-control" name="summary-award_'+input_num+'"></textarea>' +
            '</div>' +
        '</div>';
        $(".form-row").append(listcontent);
        return false;
    });
});

/*
$(".experience-info").on('click','.trash', function () {
    $(this).closest('.experience-cont').remove();
    return false;
});*/

function addWorkHighlight(x){
    var input_name = "work-highlight_form_num"+x+"";
    var input_num = parseInt($("input[name='"+input_name+"']").val());
    input_num = input_num + 1; 
    $("input[name='"+input_name+"']").val(''+input_num+'');
    var subskill = '<div class="col-10">' +
        '<div class="row form-row">' +
            '<div class="col-12">' +
                '<div class="form-group">' +
                    '<label>Highlight</label>' +
                    '<input type="text" class="form-control" name="name-work-highlight-'+x+'_'+input_num+'">' +
                '</div>' +
            '</div>' +
        '</div>' +
    '</div>' +
    '<div class="col-sm-2 col-md-2">' +
        '<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
        '<a href="#" class="btn btn-danger trash deleteData">' +
            '<i class="far fa-trash-alt"></i>' +
        '</a>' +
    '</div>'; 

    var container = ".work-highlight-"+x+"";
    $(container).append(subskill);
}
