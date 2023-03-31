from ninja import ModelSchema, Schema
from typing import List
from backend.tours_db import Tour


class Login(Schema):
    username: str
    password: str


class GetHomepage(Schema):
    own_firm: str

class GetOwnFirm(Schema):
    admin: str = None


class GetLogs(Schema):
    own_firm: str
    admin: str = None
    start_date: str = None
    end_date: str = None
    order_by: str = None
    direction: str = None


class GetAdmins(Schema):
    order_by: str = None
    direction: str = None


class GetAdminDetails(Schema):
    admin_id: int


class UpdateAdmin(Schema):
    id: int
    own_firms: List[str] = None
    name: str = None
    username: str = None
    password: str = None


class CreateAdmin(Schema):
    own_firms: List[str]
    name: str
    username: str
    password: str


class UpdateOwnFirm(Schema):
    id: int
    name: str = None
    address: str = None
    phone: str = None
    mail: str = None
    chairman: str = None
    company_place: str = None
    register_court: str = None
    tax_nr: str = None
    ustid: str = None
    contact_name: str = None
    contact_phone: str = None
    contact_fax: str = None
    bank_name: str = None
    bank_iban: str = None
    bank_bic: str = None


class CreateOwnFirm(Schema):
    name: str
    address: str = None
    phone: str = None
    mail: str = None
    chairman: str = None
    company_place: str = None
    register_court: str = None
    tax_nr: str = None
    ustid: str = None
    contact_name: str = None
    contact_phone: str = None
    contact_fax: str = None
    bank_name: str = None
    bank_iban: str = None
    bank_bic: str = None


class DeleteCustomer(Schema):
    firm_id: int


class UpdateCustomer(Schema):
    firm_id: int
    name: str = None
    vat: str = None
    address: str = None


class CreateCustomer(Schema):
    own_firm: str
    firm_name: str
    vat: str = None
    address: str = None


class GetCustomers(Schema):
    own_firm: str
    order_by: str = None
    direction: str = None


class UpdateTag(Schema):
    section: str
    id: int
    name: str = None
    colour: str = None


class CreateTag(Schema):
    section: str
    name: str
    colour: str


class DeleteTag(Schema):
    section: str
    id: int


class GetOffdays(Schema):
    own_firm: str
    month: str
    year: str
    worker: str = None
    holidays_remaining_start: str = None
    holidays_remaining_end: str = None
    tag: str = None


class UpdateOffdays(Schema):
    id: int
    tag: str = None
    notes: str = None
    dates: str = None


class CreateOffdays(Schema):
    worker_id: int
    admin: str
    tag: str
    notes: str = None
    dates: List[str]


class GetWorkers(Schema):
    own_firm: str
    order_by: str = None
    direction: str = None
    show_quit_workers: bool = None


class WorkTimeSchema(Schema):
    worker_id: int
    admin: str
    date: str
    start: str
    pause: str
    end: str
    duration: str
    daily_expenses: float = None


class AddWorkerDocument(Schema):
    worker_id: int
    admin: str
    name: str
    expiry_date: str = None
    done: bool = None


class UpdateWorkerDocument(Schema):
    document_id: int
    admin: str
    name: str = None
    expiry_date: str = None
    delete_file: bool = None
    done: bool = None


class AddDebt(Schema):
    worker_id: int
    admin: str
    amount: float
    date: str
    notes: str = None


class UpdateWorker(Schema):
    worker_id: int
    admin: str
    new_worker_id: str = None
    name: str = None
    position: str = None
    start_date: str = None
    end_date: str = None
    salary: float = None
    daily_expense: float = None
    holidays: int = None
    note: str = None
    has_quit: bool = None
    quit_date: str = None
    remaining_holidays: int = None


class CreateWorker(Schema):
    own_firm: str
    admin: str
    name: str
    worker_id: str
    position: str
    start_date: str
    salary: float
    daily_expenses: float = None
    holidays: int
    remaining_holidays: int = None
    note: str = None
    quit_date: str = None


class UpdateDebt(Schema):
    debt_id: int
    admin: str
    amount: float = None
    date: str = None
    notes: str = None


class GetDailyExpenses(Schema):
    own_firm: str
    order_by: str = None
    direction: str = None


class CreateGutschriftPayment(Schema):
    gutschrift_id: int
    admin: str
    amount: float
    date: str


class UpdateGutschrift(Schema):
    gutschrift_id: int
    admin: str
    document_nr: str = None
    firm: int = None
    creation_date: str = None
    start: str = None
    end: str = None
    gross_amount: float = None
    taxes: str = None
    avis_nr: str = None


class CreateGutschrift(Schema):
    own_firm: str
    admin: str
    firm: str
    creation_date: str
    start: str
    end: str
    document_nr: str
    gross_amount: float
    taxes: float
    avis_nr: str = None


class GetGutschrift(Schema):
    gutschrift_id: int
    order_by: str = None
    direction: str = None


class GetGutschrifts(Schema):
    own_firm: str
    firm: int = None
    avis_nr: str = None
    document_nr: str = None
    paid_start: float = None
    paid_end: float = None
    open_start: float = None
    open_end: float = None
    order_by: str = None
    direction: str = None


class ProductSchema(Schema):
    bill_id: int
    position: int
    description: str
    amount: float
    unit: str
    unit_price: float


class CreateBillSchema(Schema):
    own_firm: str
    admin: str
    firm: str
    customer_tax_nr: str
    address: str
    creation_date: str
    has_to_be_paid_date_start: str = None
    has_to_be_paid_date_end: str = None
    taxes: float
    products: str


class GetBillsSchema(Schema):
    own_firm: str
    firm: str = None
    netto_start: float = None
    netto_end: float = None
    brutto_start: float = None
    brutto_end: float = None
    created_date_start: str = None
    created_date_end: str = None
    order_by: str = None
    direction: str = None


class GetFuelcard(Schema):
    card_id: int
    order_by: str = None
    direction: str = None


class GetFuelCardsSchema(Schema):
    own_firm: str
    firm: str = None
    driver: str = None
    active: bool = None
    order_by: str = None
    direction: str = None


class GetContact(Schema):
    contact_id: str
    order_by: str = None
    direction: str = None


class GetContactsSchema(Schema):
    own_firm: str
    name: str = None
    firm: str = None
    tag: str = None
    order_by: str = None
    direction: str = None


class ChangeFuelCardDriverSchema(Schema):
    card_id: int
    admin: str
    worker_id: int
    got_date: str
    gave_back_date: str = None


class UpdateFuelcardSchema(Schema):
    card_id: int
    admin: str
    card_nr: str = None
    firm: str = None
    status: str
    notes: str = None


# class UpdateFuelcardActivity(Schema):
#     activity_id: int
#     admin: str
#     driver: str
#     got_date: str = None
#     gave_back_date: str = None



class CreateFuelCardSchema(Schema):
    own_firm: str
    admin: str
    firm: str
    card_nr: str
    status: str
    notes: str = None


class CreateMeetingSchema(Schema):
    admin: str
    meetings_notes: str = None
    meetings_date: str
    contact: int


class UpdateMeeting(Schema):
    admin: str
    meeting_id: int
    meetings_notes: str = None
    meetings_date: str = None



class UpdateContactSchema(Schema):
    contact_id: int
    admin: str
    name: str = None
    firm: str = None
    tag: str = None
    phone: str = None
    mail: str = None
    fax: str = None
    address: str = None
    note: str = None


class CreateContactSchema(Schema):
    own_firm: str
    admin: str
    name: str
    tag: str
    firm: str = None
    phone: str = None
    mail: str = None
    fax: str = None
    address: str = None
    note: str = None


class UpdateTruckDocument(Schema):
    own_firm: str
    admin: str
    document_id: int
    name: str = None
    expiry_date: str = None
    delete_file: bool = None
    done: bool = None


class ChangeTruckPayment(Schema):
    own_firm: str
    admin: str
    plate: str
    payment_method: str = None
    price: float = None
    total_installment_months: str = None
    installment_monthly_payment_amount: float = None
    paid_status: bool = None
    paid_day: str = None
    installment_start_date: str = None
    installment_end_date: str = None


class AddTruckDocumentSchema(Schema):
    own_firm: str
    admin: str
    plate: str
    name: str
    expiry_date: str = None
    done: bool = None


class CreateTruckSchema(Schema):
    own_firm: str
    admin: str
    plate: str
    manufacturer: str
    model: str


class UpdateTruck(Schema):
    own_firm: str
    admin: str
    truck_id: int
    plate: str = None
    manufacturer: str = None
    model: str = None


class GetToursSchema(Schema):
    own_firm: str
    year: str
    month: str
    firm: str = None
    status: str = None
    drivers: List[str] = None


class GetToursFilterSchema(Schema):
    own_firm: str
    start_date: str = None
    end_date: str = None


class GetTourSchema(Schema):
    own_firm: str
    roller_nr: str
    period_year: str = None
    period_month: str = None


class MitarbeiterSchema(Schema):
    vorname: str
    nachname: str
    mitarbeiter_id: str
    jaehrliche_urlaubs_tage: int
    position: str
    ist_fahrer: bool
    fahrer_karte: str = None
    fuehrerschein: str = None
    modul_95: str = None
    adr: str = None
    fuehrerschein_kontrolle: str = None
    einstiegs_datum: str
    erneut_eingestiegen: bool
    notizen: str = None


class TourDaySchema(Schema):
    own_firm: str
    admin: str
    roller_nr: str
    dates: List[str]
    status: str
    driver_list: List[str]
    note: str = None
    vehicle: str


class CreateTourSchema(Schema):
    own_firm: str
    admin: str
    roller_nr: str
    firm_name: str
    general_note: str = None
    default_driver: str = None
    default_truck: str = None


class DeleteTour(Schema):
    roller_nr: str
    own_firm: str
    admin: str


class UpdateTourSchema(Schema):
    own_firm: str
    admin: str
    query_roller_nr: str
    roller_nr: str = None
    firm_name: str = None
    general_note: str = None
    default_driver: str = None
    default_truck: str = None


class TourModelSchema(ModelSchema):
    class Config:
        model = Tour
        model_fields = '__all__'


class TrucksSchema(Schema):
    own_firm: str
    plate: str = None
    manufacturer: str = None
    model: str = None
    order_by: str = None
    direction: str = None
