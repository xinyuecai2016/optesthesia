import torch
class data_prefetcher():
    def __init__(self,loader):
        self.loader=iter(loader)
        self.stream=torch.cuda.stream()
        self.mean=torch.tensor([0.485*255,0.456*255,0.406*255])
        self.std=torch.tensor([0.229*255,0.224*255,0.225*255])
        self.perload()
    def preload(self):
        try:
            self.next_input,self.next_target=next(self.loader)
        except StopIteration:
            self.next_input=None
            self.next_target=None
            return
        with torch.cuda.stream(self.stream):
            self.next_input=self.next_input.cuda(non_blocking=True)
            self.next_target=self.next_target.cuda(non_blocking=True)
            self.next_input=self.next_input.float()
            self.next_input=self.next_input.sub_(self.mean).div_(self.std)






