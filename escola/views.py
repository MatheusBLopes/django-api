from rest_framework import viewsets, generics
from .models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer,\
                        ListaMatriculasAlunoSerializer, MatriculaSerializer,\
                        ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculasViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    """ Lista as matrículas de um aluno """
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
    """ Listando alunos matrículados em um curso """
    def get_queryset(self):
        """Cria um filtro que recebe o id do curso pela URL"""
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
