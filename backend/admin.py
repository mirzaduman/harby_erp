from django.contrib import admin
from backend.bills_db import Product, Bill
from backend.contacts_db import Contact, Meeting, ContactTag
from backend.firms_db import Firm
from backend.fuel_cards import Fuelcard, FuelcardFirm, FuelcardActivities
from backend.gutschriften_db import Gutschrift, GutschriftPayment
from backend.own_firms_db import OwnFirm
from backend.tours_db import DailyNote, TourStatus, Tour, TourDay
from backend.trucks_db import Truck, TruckDocument
from backend.workers_db import Position, Worker, DebtPayment, WorkerActivity, HolidayAccount, OffdayTag, Offday, \
    WorkerDocument, WorkTime
from backend.settings_db import Colour, HarbyAdmin, Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin', 'timestamp', 'log_input')


@admin.register(HarbyAdmin)
class HarbyAdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(Colour)
class ColourAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'colour_hex')


@admin.register(WorkTime)
class WorkTimeAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkerDocument)
class WorkerDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'worker', 'upload_date', 'name')


@admin.register(Offday)
class OffdayAdmin(admin.ModelAdmin):
    list_display = ('id', 'worker', 'tag', 'date')


@admin.register(OffdayTag)
class OffdayTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(HolidayAccount)
class HolidayAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'worker', 'used_holiday_days')


@admin.register(WorkerActivity)
class WorkerActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'worker', 'date')


@admin.register(DebtPayment)
class DebtPaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'worker', 'amount')


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'own_firm', 'name', 'worker_id')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(TruckDocument)
class TruckDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ('id', 'own_firm', 'plate')


@admin.register(TourDay)
class TourDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'tour', 'date')


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('id', 'roller_nr', 'firm')


@admin.register(TourStatus)
class TourStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(DailyNote)
class DailyNoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'note')


@admin.register(OwnFirm)
class OwnFirmAdmin(admin.ModelAdmin):
    pass


@admin.register(GutschriftPayment)
class GutschriftPaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'gutschrift', 'amount', 'date')


@admin.register(Gutschrift)
class GutschriftAdmin(admin.ModelAdmin):
    list_display = ('id', 'firm', 'creation_date', 'document_nr')


@admin.register(FuelcardActivities)
class FuelcardActivitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver', 'fuelcard', 'got_date')


@admin.register(Fuelcard)
class FuelcardAdmin(admin.ModelAdmin):
    list_display = ('id', 'card_nr')


@admin.register(FuelcardFirm)
class FuelcardFirmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short')


@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    list_display = ('id', 'own_firm', 'name')


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('id', 'meetings_date', 'contact')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'own_firm')


@admin.register(ContactTag)
class ContactTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'own_firm', 'firm', 'bill_nr')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'amount')
