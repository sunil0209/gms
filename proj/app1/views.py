from django.shortcuts import render, get_object_or_404, redirect
from .models import Complaint
from .forms import ComplaintForm
def create_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaint_list')  # Redirect to a view that lists all complaints
    else:
        form = ComplaintForm()

    return render(request, 'complaint/create_complaint.html', {'form': form})

def update_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, pk=complaint_id)

    if request.method == 'POST':
        form = ComplaintForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            return redirect('complaint_list')  # Redirect to a view that lists all complaints
    else:
        form = ComplaintForm(instance=complaint)

    return render(request, 'complaint/update_complaint.html', {'form': form})
# views.py
def complaint_list(request):
    complaints = Complaint.objects.all()
    return render(request, 'complaint/complaint_list.html', {'complaints': complaints})

# Create your views here.

def delete_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, pk=complaint_id)
    if request.method == 'POST':
        form = ComplaintForm(request.POST, instance=complaint)
        complaint.delete()
        return redirect('complaint_list')  # Redirect to a view that lists all complaints
    else:
        form = ComplaintForm(instance=complaint)
    return render(request, 'complaint/delete_complaint.html', {'form': form})

