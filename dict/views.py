from kvintang.dict.models import Tag, Term, Subject
from kvintang.render import render_response
from django.shortcuts import redirect
from django.http import Http404

import os


def getContext():
    context = {"terms" : Term.objects.all(),
               "subjects" : Subject.objects.all(),
               "tags" : Tag.objects.all() 
               }
    
    return context
    
    
def base(request):
    context = getContext()
    return render_response(request, "base.html", context)

def search(request, *args, **kwargs):
    context = getContext()

    term = request.GET.get("term")
    
    loots = Term.objects.filter(englishVersion__icontains = term)
    if not loots:
        loots = Term.objects.filter(czechVersion__icontains = term)

    
    context["loots"] = loots
    context["title"] = term

    
    return render_response(request, "results.html", context)

def byTag(request, tag):
    tagObj = Tag.objects.get(id= tag)
    loots = Term.objects.filter(tags=tagObj).order_by("englishVersion")

    context = getContext()
    context["loots"] = loots
    context["title"] = tagObj.name
      
    return render_response(request, "results.html", context)

def bySubject(request, subject):
    subObj = Subject.objects.get(id= subject)
    loots = Term.objects.filter(subject=subObj).order_by("englishVersion")
    
    context = getContext()
    context["loots"] = loots
    context["title"] = subObj.name
    
    return render_response(request, "results.html", context)


def export(request):
    context = getContext()
    context["title"] = "Export"

    return render_response(request, "exportMain.html", context)

def exportByTag(request, tag):
    tagObj = Tag.objects.get(id= tag)
    loots = Term.objects.filter(tags=tagObj).order_by("englishVersion")
    context = getContext()
    context["loots"] = loots
    context["title"] = tagObj.name
      
    return render_response(request, "export.html", context)

def exportBySubject(request, subject):
    subObj = Subject.objects.get(id= subject)
    loots = Term.objects.filter(subject=subObj).order_by("englishVersion")
    
    context = getContext()
    context["loots"] = loots
    context["title"] = subObj.name
    
    return render_response(request, "export.html", context)

def exportStar(request):
    tabfile = "/home/visgean/kvintang/stardict/kvintang.tab"
    tabfilebin = "/usr/lib/stardict-tools/tabfile"
    
    fileObj = open(tabfile, "w")
    #data = ["%s\t%s" % (trm.englishVersion, trm.czechVersion) for trm in Term.objects.all()]
    data = ""
    for term in Term.objects.all():
        data += "%s\t%s\n" % (term.englishVersion, term.czechVersion)


    fileObj.write(data)
    fileObj.close()

    os.system("%s %s" % (tabfilebin, tabfile))
    return redirect("/static/stardict/kvintang.dict.dz")

